# AI Voice Assistant Mini Project

## Overview
This is a simple AI-based voice assistant built with Python. It listens to voice commands and performs basic tasks like opening WhatsApp, YouTube, Google, or writing spoken text to Notepad.

## Features
- Open WhatsApp (desktop app)
- Open YouTube (in browser)
- Open Google (in browser)
- Write spoken text to a file and open it in Notepad

## Requirements
- Python 3.x
- Libraries: pyttsx3, SpeechRecognition, pyaudio, webbrowser, os-sys

## Setup
1. Install dependencies: `pip install pyttsx3 SpeechRecognition pyaudio webbrowser os-sys`
2. Update the WhatsApp path in `task_handler.py` to match your system.
3. Run `main.py` to start the assistant.

## Usage
Say commands like:
- "Open WhatsApp"
- "Open YouTube"
- "Open Google"
- "Write [your text]"
- "Exit" to stop

## Notes
- Requires a working microphone.
- WhatsApp path is Windows-specific; adjust for other OS if needed.