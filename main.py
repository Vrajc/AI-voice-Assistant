import voice_engine
import task_handler

def run_assistant():
    voice_engine.speak("Hello! I'm your AI assistant. How can I help you today?")
    while True:
        command = voice_engine.listen()
        if command:
            if "exit" in command.lower() or "stop" in command.lower():
                voice_engine.speak("Goodbye!")
                break
            else:
                task_handler.handle_task(command)
        else:
            voice_engine.speak("Sorry, I didn’t catch that. Please try again.")

if __name__ == "__main__":
    print("Starting Voice Assistant...")
    run_assistant()