#!/usr/bin/env python3
import openai

def chat_completion(messages, model="gpt-3.5-turbo"):
    return openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        max_tokens=2048,
    )

class GPTChat:
    def __init__(self, first_prompt=None, system_prompt=None, model="gpt-3.5-turbo"):
        self.model = model
        self.messages = []
        self.completions = []
        if system_prompt is not None:
            self.append_content(system_prompt, role='system')
        if first_prompt is not None:
            self.append_content(first_prompt)
    def append_content(self, content, role='user'):
        self.append_message({
            "role": role,
            "content": content
        })
    def append_message(self, message):
        self.messages.append(message)
    def forward(self):
        completion = chat_completion(self.messages, model=self.model)
        self.completions.append(completion)
        self.append_message(dict(completion.choices[0].message))
