import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init() 

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        musicLibrary.music[song]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        speak(f"Playing {song}")

if __name__ == ('__main__'):
    speak("Initializing........")

    while True:
        r = sr.Recognizer()
        
        print("Recognizing")
        try:
            with sr.Microphone() as source:
                print("Say Something!")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)

            command = r.recognize_google(audio)
            if(command.lower() == "tejas"):
                speak("YES")
                with sr.Microphone() as source:
                    print("Say Command")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)



        except Exception as e:
            print("Error\n ; {0}".format(e))
        