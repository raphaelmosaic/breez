#!/usr/bin/env python3
import time
import json
import re
import requests
from pynput import keyboard
from pynput.keyboard import Key
from pyperclip import copy, paste
import subprocess
import json
import os

# Load Configuration from JSON
config_data = {}
config_path = 'config.json'
if os.path.exists(config_path):
    with open(config_path, 'r') as f:
        config_data = json.load(f)

OPENAI_API_KEY = config_data.get('api_key', "YOUR_DEFAULT_API_KEY")
HOTKEY = config_data.get('hotkey', "Double tap CMD")

cmd_down = False
shift_down = False

# Hotkey actions
hotkey_actions = {
    "F10": lambda key, current_time: on_activate() if key == Key.f10 else None,
    "CMD + .": lambda key, current_time: on_activate() if key == keyboard.KeyCode.from_char('.') and cmd_down else None,
    "CMD + :": lambda key, current_time: on_activate() if key == keyboard.KeyCode.from_char(':') and cmd_down else None,
}


# -------------- Function to call OpenAI GPT API for text correction —---------—--
def call_gpt3_api(text):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    data = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"Fix the typos without adding anything to it, do not describe what you did just output the corrected text. If the text has a markdown format keep it. Text to correct:{text}"}],
        "temperature": 0.7,
    })
    response = requests.post(url, headers=headers, data=data)
    response_data = response.json()
    if "choices" not in response_data:
        print(f"Error with GPT-3 API call: {response_data}")
        return ""
    fixed_text = response_data["choices"][0]["message"]["content"].strip()
    fixed_text = fixed_text.replace('"', '')
    return fixed_text
# ---------------------------------------------------------------------------------

def cmd_c():
    controller = keyboard.Controller()
    time.sleep(0.1)
    controller.press(Key.cmd)
    controller.press('c')
    time.sleep(0.05)
    controller.release('c')
    controller.release(Key.cmd)
    time.sleep(0.05)

def cmd_a():
    controller = keyboard.Controller()
    time.sleep(0.1)
    controller.press(Key.cmd)
    controller.press('a')
    controller.release('a')
    controller.release(Key.cmd)
    time.sleep(0.1)

def cmd_v():
    controller = keyboard.Controller()
    time.sleep(0.1)
    controller.press(Key.cmd)
    controller.press('v')
    controller.release('v')
    controller.release(Key.cmd)
    time.sleep(0.1)

def checkif_active_window(app_name):
    script = 'tell application "System Events" to set frontApp to name of first application process whose frontmost is true'
    front_app = subprocess.check_output(["osascript", "-e", script]).strip().decode("utf-8")
    return front_app == app_name

# Heptabase
def select_current_line_in_heptabase():
    cmd_a()
    cmd_c()

# Notion
def select_current_line_in_notion():
    cmd_a()
    cmd_c()

# iA Writer
def select_current_line_in_ia_writer():
    controller = keyboard.Controller()
    with controller.pressed(Key.alt):
        controller.press(Key.down)
        controller.release(Key.down)
    time.sleep(0.1)
    with controller.pressed(Key.alt, Key.shift):
        controller.press(Key.up)
        controller.release(Key.up)
    cmd_c()

# General current line
def select_current_line_general():
    controller = keyboard.Controller()
    with controller.pressed(Key.cmd):
        controller.press(Key.right)
        controller.release(Key.right)
    time.sleep(0.1)
    with controller.pressed(Key.cmd, Key.shift):
        controller.press(Key.left)
        controller.release(Key.left)
    cmd_c()
    
# Main function to be triggered on hotkey press
def on_activate():
    copied_text = None  # Initialize to None for safety

    if checkif_active_window("iA Writer"):
        select_current_line_in_ia_writer()
    elif checkif_active_window("Notion"):
        select_current_line_in_notion()
    elif checkif_active_window("Heptabase"):
        select_current_line_in_heptabase()
    else:
        select_current_line_general()

    copied_text = paste()

    if copied_text:  # Only proceed if copied_text is not None or empty
            whitespace, content = re.match(r'(\s*-?\s*)(.*)', copied_text).groups()
            fixed_text = call_gpt3_api(content)
            final_text = whitespace + fixed_text
            copy(final_text)
            cmd_v()


def on_press(key):
    global cmd_down
    current_time = time.time()

    if key == Key.cmd:  # Handle CMD key
        cmd_down = True

    # Only execute the function corresponding to the defined HOTKEY
    if HOTKEY in hotkey_actions:
        hotkey_actions[HOTKEY](key, current_time)

def on_release(key):
    global cmd_down
    if key == Key.cmd:
        cmd_down = False


# Listen to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()