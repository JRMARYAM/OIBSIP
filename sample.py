import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""
        return query.lower()

def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak(f"The time is {current_time}")

def tell_date():
    now = datetime.datetime.now()
    current_date = now.strftime("%B %d, %Y")
    speak(f"Today's date is {current_date}")

def search_web(query):
    speak(f"Searching for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")

def main():
    speak("Hello, how can I assist you today?")
    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I help you?")
        elif "time" in query:
            tell_time()
        elif "date" in query:
            tell_date()
        elif "search for" in query:
            search_query = query.replace("search for", "").strip()
            if search_query:
                search_web(search_query)
            else:
                speak("What do you want me to search for?")
        elif "stop" in query or "exit" in query or "bye" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm not sure how to help with that.")

if __name__ == "__main__":
    main()
