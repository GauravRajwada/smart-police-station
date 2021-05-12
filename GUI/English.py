import pyttsx3
import datetime
import databse as c
import send_details as send
from GUI import Victim_GUI as g

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
voice = voices[1]
engine.setProperty('voice', voice.id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def welcome():
    # it give us the hour in 0 to 24
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        print("Good morning")
    elif hour >= 12 and hour < 16:"""
         print("Good afternoon")
"""
        .command("Good afternoon")

    elif hour >= 16 and hour < 20:
        print("Good evening")
    else:
        print("Dont panic, We will help you Relax")
    print('Welcome to Smart Police Station')
    print('I am your assistant Zara. I am here to help you.')

def main():
    welcome()
    print("Enter Your Adhaar Card number")
    number = int(input())
    form=c.adhaar(number)
    print('Your personal identification details are:')
    for i in form.keys():
        if i=="Adhaar_no":
            print("Adhaar card number" + ": " + str(form[i]))
        else:
            print(str(i)+": "+str(form[i]))

    print("Please tell the details ")
    print("Date of incident")
    form["Date_of_incident"] = input()
    print('Place of incident')
    form['Place_pf_incident'] = input()
    print('Please give the description')
    form['Description'] = input()
    form["Victim_Name"] = form.pop("Name")
    form['Investigating_officer'] = str(c.min_case_off())
    c.fir_register(form)
    send.send_message()
    print("All the details has been send successfully.")







