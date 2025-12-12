
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import os



def convert_speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said - ",text)
            return text
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            
def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

while True:
    text = "I am listening"
    text_to_speech(text)
    command = convert_speech_to_text()
    command = command.lower()

    if 'open youtube' in command:
        wb.open("https://www.youtube.com")

    elif 'open google' in command:
        wb.open("https://www.google.com")

    elif 'wikipedia' in command:
        topic = input("Enter topic to search on Wikipedia: ")
        url = "https://en.wikipedia.org/wiki/" + topic.replace(" ", "_")
        wb.open(url)

    elif 'open instagram' in command:
        wb.open("https://www.instagram.com")

    elif 'control panel' in command:
        os.system("control")
    
    elif 'command prompt' in command:
        os.system("cmd")
    elif 'notepad' in command:
        os.system("notepad")
    elif 'calculator' in command:
        os.system("calc")
    elif 'camera' in command:
        os.system("start microsoft.windows.camera:")

    elif 'exit' in command:
        text_to_speech("Goodbye! see you again")
        break

    else:
        text_to_speech("I don't know")



# text =convert_speech_to_text()
# text_to_speech(text)
