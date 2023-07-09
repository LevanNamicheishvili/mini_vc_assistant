import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand.")
    except sr.RequestError:
        print("Sorry, there was an issue with the service.")

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def process_input(input):
    # Example: Simple greeting response
    if "hello" in input.lower():
        speak("Hello! How can I assist you?")
    elif "goodbye" in input.lower():
        speak("Goodbye!")
        exit()

# Main loop
while True:
    user_input = listen()
    process_input(user_input)
