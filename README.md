🤖 Jarvis – Voice Assistant

A simple **Python-based voice assistant** that listens to voice commands, recognizes speech, and performs different tasks such as opening websites, applications, and providing the current date and time.

👩‍💻 Author

**Kavya Balsaraf**
Electronics & Telecommunication Engineering

---

📌 Project Overview

**Jarvis** is a beginner-friendly voice assistant developed using Python. It uses a microphone to receive voice input and **Google Speech Recognition** to convert speech into text.

The assistant continuously listens for the wake word **"Jarvis"**. Once the wake word is detected, Jarvis becomes active and can execute commands such as:

* Tell the current time
* Tell today's date
* Tell the current month
* Tell the current year
* Open Google
* Open YouTube
* Open WhatsApp
* Open ChatGPT
* Open Calculator
* Open Google Chrome
* Open Visual Studio Code
* Open Arduino IDE
* Open Microsoft Word
* Open Microsoft Excel

---

 ✨ Features

* 🎙️ Voice input using microphone
* 🗣️ Speech-to-text using Google Speech Recognition
* 🔊 Text-to-speech response using `pyttsx3`
* 👂 Wake word detection using **"Jarvis"**
* 🌐 Open websites using voice commands
* 💻 Launch Windows applications
* 🕐 Get current time
* 📅 Get current date
* 📆 Get current month and year
* 🛑 Stop command mode using the **"stop"** command

---

🛠️ Technologies Used

| Technology                | Purpose                       |
| ------------------------- | ----------------------------- |
| Python                    | Main programming language     |
| SpeechRecognition         | Converts voice into text      |
| Google Speech Recognition | Speech recognition service    |
| pyttsx3                   | Text-to-speech                |
| Webbrowser                | Opens websites                |
| urllib.parse              | Handles URL search parameters |
| subprocess                | Opens Windows applications    |
| datetime                  | Provides date and time        |

---

## 📂 Project Structure

```text
Jarvis/
│
├── main.py
│
├── README.md
│
└── requirements.txt
```

> The main Python file can be named according to the file used in your GitHub repository.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project folder:

```bash
cd Jarvis
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Required Libraries

```bash
pip install SpeechRecognition pyttsx3 PyAudio
```

If you are using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python program:

```bash
python main.py
```

Jarvis will start with:

```text
Jarvis: Initializing Jarvis
```

The program will then listen for the wake word.

Say:

```text
Jarvis
```

Jarvis will respond:

```text
Yes
Jarvis Activated
```

You can then give a command.

---

## 🎤 Voice Commands

### Date and Time

```text
What is the time?
```

```text
What is today's date?
```

```text
What is the current month?
```

```text
What is the current year?
```

### Websites

```text
Open Google
```

```text
Open YouTube
```

```text
Open WhatsApp
```

```text
Open ChatGPT
```

### Applications

```text
Open Calculator
```

```text
Open Chrome
```

```text
Open VS Code
```

```text
Open Arduino
```

```text
Open Word
```

```text
Open Excel
```

### Stop Jarvis

Say:

```text
Stop
```

Jarvis will respond:

```text
Going to sleep
```

and return to wake-word listening mode.

---

## 🔄 Working Flow

```text
          Start Jarvis
                ↓
        Initialize Assistant
                ↓
       Listen Through Microphone
                ↓
       Detect "Jarvis" Wake Word
                ↓
        Jarvis Gets Activated
                ↓
        Listen for Command
                ↓
       Convert Speech to Text
                ↓
         Process Command
                ↓
     ┌──────────┴──────────┐
     ↓                     ↓
Perform Action        Give Voice Response
     ↓                     ↓
Open App/Website       Continue Listening
     │
     └──────────────→ Stop Command
                           ↓
                    Return to Sleep
```

---

## 🧠 How It Works

### 1. Speech Recognition

The `SpeechRecognition` library captures audio from the microphone.

```python
with sr.Microphone() as source:
    audio = r.listen(source)
```

The recorded audio is converted into text using:

```python
r.recognize_google(audio)
```

### 2. Wake Word Detection

Jarvis checks whether the recognized speech contains the word:

```text
Jarvis
```

If detected, the assistant becomes active.

### 3. Command Processing

The `processCommand()` function checks the user's command and performs the corresponding action.

For example:

```text
Open YouTube
```

opens YouTube in the web browser.

### 4. Text-to-Speech

The `pyttsx3` library allows Jarvis to speak its responses.

```python
engine.say(text)
engine.runAndWait()
```

### 5. Application Launching

Windows applications are launched using Python's `subprocess` module.

Example:

```python
subprocess.Popen("calc.exe")
```

---

## 🎙️ Speech Recognition Test

The project also contains a simple microphone testing program that can be used to check whether speech recognition is working correctly.

Example:

```python
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)

except sr.UnknownValueError:
    print("Could not understand your voice")

except sr.RequestError as e:
    print("Google Speech Recognition error:", e)
```

This test helps verify:

* Microphone access
* Speech recognition
* Internet connection
* Google Speech Recognition service

---

## ⚠️ Important Notes

* An active internet connection is required for Google Speech Recognition.
* A working microphone is required.
* Windows application paths may be different on different computers.
* The Chrome, Word, Excel, and Arduino paths may need to be changed according to your installation location.
* `PyAudio` is required for microphone input.

---

## 🚀 Future Improvements

The project can be extended with:

* 🔎 Google and YouTube voice search
* 📁 File and folder management
* 📧 Email sending
* 🎵 Music control
* 🌦️ Weather information
* 📰 News updates
* 🤖 AI chatbot integration
* 🔐 User authentication
* 🗣️ More natural voice responses
* 🧠 Custom wake-word detection
* 📱 Mobile application integration

---

## 🎯 Project Objective

The main objective of this project is to develop a simple voice-controlled personal assistant using Python and understand the basic concepts of:

* Speech recognition
* Natural language commands
* Text-to-speech
* Python automation
* Voice-controlled application launching

## 👩‍💻 Author
**Kavya Balsaraf**

