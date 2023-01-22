import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takecommand():
    try:
        with sr.Microphone() as source:
            print("Say something!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri','')
                talk(command)
                print(command)

    except:
        pass

    return command

def runSiri():
    command = takecommand()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M:%S')
        print(time)
        talk('Currently time is ' + time)
    elif 'what is' in command:
        index = command.replace('what is', '')
        info = wikipedia.summary(index,1)
        print(info)
        talk(info)
    elif 'new year' in command:
        talk("新年快乐，万事如意，心想事成，笑口常开，红包一百万给你")
    else:
        talk("Sorry,Please say the command again.")


while True:
    runSiri()
    

