import speech_recognition as sr
import webbrowser
import urllib.parse
import pyttsx3
import subprocess
from datetime import datetime

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def processCommand(c):
    c = c.lower()

    if "time" in c:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in c:
        today = datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "month" in c:
        month = datetime.now().strftime("%B")
        speak(f"The current month is {month}")

    elif "year" in c:
        year = datetime.now().year
        speak(f"The current year is {year}")
        

    elif "open google" in c:
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open whatsapp" in c:
        webbrowser.open("https://whatsapp.com")
        
    elif "chatgpt" in c or "chat gpt" in c:
        webbrowser.open("https://chatgpt.com")
        
    elif "open calculator" in c:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")
        
    elif "open chrome" in c:
        speak("Opening Chrome")
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    elif "open vs code" in c or "open visual studio code" in c:
        speak("Opening Visual Studio Code")
        subprocess.Popen("code")

    elif "open arduino" in c or "open arduino uno" in c:
        speak("Opening Arduino")
        subprocess.Popen("arduino.exe")

    elif "open word" in c or "open ms word" in c:
        speak("Opening Microsoft Word")
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")

    elif "open Excel" in c or "open ms excel" in c:
        speak("Opening Microsoft Excel")
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\Excel.exe")

if __name__ == "__main__":

    speak("Initializing Jarvis")

    while True:

        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                print("\nListening for wake word...")

                audio = r.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=5
                )

            word = r.recognize_google(audio)

            print("You said:", word)

            if "jarvis" in word.lower():

                print("Wake word detected")

                speak("Yes")
                speak("Jarvis Activated")

                while True:

                    try:

                        with sr.Microphone() as source:

                            print("\nListening for command...")

                            audio = r.listen(
                                source,
                                timeout=5,
                                phrase_time_limit=5
                            )

                        command = r.recognize_google(audio)

                        print("Command:", command)

                        # Stop command mode
                        if "stop" in command.lower():
                            speak("Going to sleep")
                            break

                        # Execute command
                        processCommand(command)

                    except sr.WaitTimeoutError:
                        print("No command detected")

                    except sr.UnknownValueError:
                        print("I could not understand the command")

                    except sr.RequestError as e:
                        print("Speech recognition error:", e)

        except sr.WaitTimeoutError:
            print("No wake word detected")

        except sr.UnknownValueError:
            print("Could not understand")

        except sr.RequestError as e:
            print("Speech recognition error:", e)