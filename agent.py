#!/usr/bin/env python
import docker_handler
import openai
import sys
import time
from datetime import datetime
import json
import regex
from tqdm import trange
from werkzeug.utils import secure_filename
from chatgpt_controller import GPTChat
import os

openai.api_key = os.environ['OPENAI_API_KEY']

JSON_EXTRACTOR = regex.compile(r'{(?:[^{}]*|(?R))*}')

def add_ellipsis(s, k=2000):
    return s if len(s) <= k else f"[...] {s[-k:]}"

def build_markdown():
    return f"**Goal:** {goal}\n```\n{virtual_shell} " + ''.join([f"{ai_move['command']}\n```\n> _GPT:_ {ai_move['comments']}\n```\n{add_ellipsis(ai_move['response'])}" for ai_move in ai_moves]) + "\n```"

def extract_json(s):
    print(s)
    return JSON_EXTRACTOR.findall(s)[0]


gpt_model = sys.argv[1]
goal = sys.argv[2]

process = docker_handler.create_container()
out = docker_handler.send_command('', process)
virtual_shell = out.strip()
today = datetime.now().strftime('%A, %-d %B %Y')

sys_prompt = f"""You are a clever AI software and developer.
Today is {today}.
Your goal is to {goal}.
Once your goal is achieved, you stop.
You operate as root on a CLI-only machine running Ubuntu 20.04 with no interactivity.
At each move, you see what the terminal shows.
Return only the command in your next immediate move in a JSON object: {{"command": "your command", "comments": "your comments"}}. Do not return anything else."""
print(sys_prompt)

chat = GPTChat(f"{virtual_shell}", system_prompt=sys_prompt, model=gpt_model)

ai_moves = []

while True:
    
    try:
        print(f"Sending request to OpenAI ({len(chat.messages)} messages)...")
        try:
            chat.forward()
        except openai.InvalidRequestError:
            # remove old messages (keeping system prompt) from chat.messages and repeat
            chat.messages = chat.messages[0:1] + chat.messages[3:]
            continue
    except (openai.error.RateLimitError, openai.error.APIConnectionError) as e:
        print(f"\n\nPROCESS EXITED: {e}")
        docker_handler.send_command('exit', process)
        break

    try:
        msg_content = chat.messages[-1]['content']
        ai_move = json.loads(extract_json(msg_content))
        ai_moves.append(ai_move)
        print(f"Move #{len(ai_moves)}\n{ai_move}")
    except (json.JSONDecodeError, IndexError) as e:
        ai_move = {'command': '', 'comments': msg_content}
        ai_moves.append(ai_move)

    if ai_move['command'] in ['', 'exit']:
        ai_move['response'] = ''
        process.close()
        break

    os_response = docker_handler.send_command(ai_move['command'], process)
    ai_move['response'] = os_response
    print(os_response[-2000:])

    chat.append_content(f"{os_response[-2000:]}\n{virtual_shell}")
    
    for _ in trange(25, desc="Waiting 25 seconds...", ncols=100):
        time.sleep(1)

# Jupyter/CLI output
print(f"{virtual_shell} " + ''.join([f"{ai_move['command']}\n\x1b[1;31m{ai_move['comments']}\033[0m\n{ai_move['response']}" for ai_move in ai_moves]))

# Markdown output
md = build_markdown()

with open(f"runs/{gpt_model}_{secure_filename(goal)}.md", 'w') as f_out:
    f_out.write(md)
    print(md)
