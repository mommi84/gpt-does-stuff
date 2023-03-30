#!/usr/bin/env python3
import re
import pexpect
import time

ANSI_CLEANER = re.compile(r"(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]")
HOST_EXTRACTOR = re.compile(r'\]0;([^@]+@\w{12}).*')

PATIENCE = 5.0

def strip_colours(s):
    return ANSI_CLEANER.sub("", s)

def create_container():
    bash_command = 'docker run --rm -it --entrypoint /bin/bash ubuntu:20.04'
    child = pexpect.spawn(bash_command, timeout=PATIENCE)
    time.sleep(PATIENCE)
    return child

def extract_host(s):
    return HOST_EXTRACTOR.search(s).group(1)

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)

def build_output(child, output_list):
    before = child.before.decode('utf-8')
    try:
        host = extract_host(before)
        index = find_2nd(before, host)
    except AttributeError:
        index = 0
    output = '\n'.join(output_list[1:])
    return f"{output}\n{before[index:]}"

def send_command(command, child, verbose=False):
    output_list = []
    child.sendline(command)

    while True:
        try:
            line = child.readline().decode('utf-8').replace('\r\n', '')
            if verbose:
                print(line)
            output_list.append(strip_colours(line))
        except:
            break
    
    return build_output(child, output_list)

