import os
import webbrowser
import voice_engine
import os
import webbrowser
import urllib.parse




def handle_task(command):
    """Handle the user's command and execute the appropriate task."""

    if "open whatsapp" in command:
        voice_engine.speak("Opening WhatsApp")
        os.system("start whatsapp://")

    elif "open canva" in command:
        voice_engine.speak("Opening Canva")
        os.startfile(r"C:\Users\Asus\AppData\Local\Programs\Canva\Canva.exe")

    elif "open reel" in command:
        voice_engine.speak("Opening Reel")
        os.startfile(r"C:\Users\Asus\OneDrive\Desktop\vrajreel.mp4")
    
    elif "open youtube" in command:
        voice_engine.speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    
    elif "open google" in command:
        voice_engine.speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open w3schools" in command:
        voice_engine.speak("Opening w3schools")
        webbrowser.open("https://www.w3schools.com/")
    
    elif "open chat" in command:
        voice_engine.speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com/")

    elif "play song" in command or "play music" in command:
        voice_engine.speak("Which song would you like to play?")
        song_name = voice_engine.listen()

        if song_name:
            voice_engine.speak(f"Playing {song_name} on Spotify.")

            # Encode the song name for a URL search
            query = urllib.parse.quote(song_name)
            os.system(f"start spotify:search:{query}")
    
        else:
            voice_engine.speak("I didn’t hear any song name.")
    


    elif "write" in command or "type" in command:
        voice_engine.speak("Please say what you want to write in Notepad.")
        text = voice_engine.listen()

        if text:
            voice_engine.speak(f"Writing: {text}")

            # Define file path (creating a temporary file)
            file_path = "C:\\Users\\Public\\notepad_text.txt"  # Change if needed

            # Write the text to the file
            with open(file_path, "w") as file:  # "w" creates a new file every time
                file.write(text)

            # Open the file in Notepad
            os.system(f'notepad.exe {file_path}')
        else:
            voice_engine.speak("I didn’t hear anything to write.")

    else:
        voice_engine.speak("I don’t understand that command. Try saying 'open something' or 'write something'.")