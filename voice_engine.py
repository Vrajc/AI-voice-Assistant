import pyttsx3
import speech_recognition as sr

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

# Initialize speech recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user voice input and return the command."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        try:
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio).lower()  # Use Google’s free API
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            speak("Sorry, there’s an issue with the speech service.")
            return None
        except sr.WaitTimeoutError:
            return None