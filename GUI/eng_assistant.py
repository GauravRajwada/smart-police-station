import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import databse as c
import send_details as send

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
voice = voices[1]
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        takecommand()
    return query


def welcome():
    # it give us the hour in 0 to 24
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon")
    elif hour >= 16 and hour < 20:
        speak("Good evening")
    else:
        speak("Dont panic, We will help you Relax")
    print('Welcome to Smart Police Station')
    speak('Welcome to Smart Police Station')
    print('I am your assistant Zara. I am here to help you.\nEnter Your Adhaar Card number')
    speak("I am your assistant Zara. I am here to help you.\nEnter Your Adhaar Card number")

def main():
    welcome()
    number = int(input())
    form=c.adhaar(number)
    print('Your personal identification details are:')
    speak('Your personal identification details are:')
    for i in form.keys():
        if i=="Adhaar_no":
            print("Adhaar card number" + ": " + str(form[i]))
            speak("Adhaar card number"+ ": " + str(form[i]))
        else:
            print(str(i)+": "+str(form[i]))
            speak(str(i) + ": " + str(form[i]))

    print("Please tell the details ")
    speak("Please tell the details ")
    print("Date of incident")
    speak("Date of incident")
    form["Date_of_incident"] = takecommand()
    print('Place of incident')
    speak('Place of incident')
    form['Place_pf_incident'] = takecommand()
    print('Please give the description')
    speak('Please give the description')
    form['Description'] = takecommand()
    form["Victim_Name"] = form.pop("Name")
    form['Investigating_officer'] = str(c.min_case_off())
    print(form)
    c.fir_register(form)
    print(form)
    send.send_message()
    print("All the details has been send successfully.")
    speak("All the details has been send successfully.")







