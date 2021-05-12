from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import datetime
from googletrans import Translator
import warnings
import databse as db
import send_details as send
from face_capture import face_capture
import sys
import os
import base64
from verification import fingure_print as verify

warnings.filterwarnings('ignore', message='Unverified HTTPS request')


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("मैं सुन रही..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("समझ रही...")
        query = r.recognize_google(audio, language='hi-in')
        print(f"आपने बोला: {query}\\n")

    except Exception as e:
        print(e)
        print("कृपया इसे फिर से दोहराएं...")
        takecommand()
    return query


def speak(query):
    audio_created = gTTS(text=query, lang="hi", slow=False)
    audio_created.save("my_file.mp3")
    playsound('my_file.mp3')
    os.remove('my_file.mp3')


def welcome():
    # it give us the hour in 0 to 24
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        print(
            "शुभ प्रभात । \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
        speak(
            "शुभ प्रभात। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
    elif hour >= 12 and hour < 16:
        print(
            "नमस्कार। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
        speak(
            "नमस्कार। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
    elif hour >= 16 and hour < 20:
        print(
            "सुसंध्या। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
        speak(
            "सुसंध्या। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
    else:
        speak(
            "घबराइए मत हम आपकी मदद करने के लिए यहां हैं।\nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")


def load_file(text):
    with open(text, 'rb') as f:
        photo = f.read()

    encodestring = base64.b64encode(photo)
    return encodestring


def main():
    translator = Translator()
    welcome()
    number = int(input())
    print('आपकी व्यक्तिगत पहचान के विवरण हैं')
    speak('आपकी व्यक्तिगत पहचान के विवरण हैं')
    form=db.adhaar(number)
    #print(translator.translate(text=str("Name")+": "+str("Gaurav"), dest='hi', src='en').text)
    for i in form.keys():
        if i == 'Name':
            temp = translator.translate(text=str(i)+": "+str(form[i]), dest='hi', src='en').text
            speak(temp)
            print(temp)
        elif i == 'DOB':
            print("जन्म तिथि " + form[i])
        elif i == 'Mobile no':
            print("मोबाइल नंबर " +str(form[i]))
        elif i == 'E-mail':
            print("ई-मेल " + str(form[i]))
        elif i=="Adhaar_no":
            print("आधार कार्ड नंबर "+str(form[i]))
        elif i=="Gender":
            print("लिंग " +form[i])
        elif i=="Mobile":
            print("मोबाइल नंबर "+str(form[i]))


    print("कृपया अपने अंगूठे को फिंगरप्रिंट प्रिंट स्कैनर में रखें।")
    print("कृपया प्रतीक्षा करें कि सत्यापन प्रक्रिया में है।")

    tryy = 3
    while not verify.fingure(form["Adhaar_no"]):
        print("अंगुली की छाप प्रिंट सत्यापित नहीं किया कृपया अपनी उंगलियों की सफाई के बाद फिर से प्रयास करें।\nतुम्हारे पास ही है {} मौका बचा।".format(tryy))
        tryy = tryy - 1
        if tryy:
            pass
        else:
            print("आप अधिक से अधिक संख्या में प्रयास करें।")
            sys.exit()
    else:
        print("फिंगर प्रिंट सक्सेसली वेरिफाइड")

    print("कृपया कैमरे का उल्लंघन करें।")
    tryy=3
    while not face_capture.capture():
        print("चेहरा पहचाना नहीं गया था कृपया चेहरे से सभी रुकावटों को हटाने के बाद फिर से कोशिश करें। कैमरा के सामने चेहरा स्पष्ट रूप से होना चाहिए।")
        tryy=tryy-1
        if tryy:
            pass
        else:
            print("आप अधिक से अधिक संख्या में प्रयास करें।")
            sys.exit()
    else:
        print("चेहरे पर सफलतापूर्वक कब्जा कर लिया गया है")

    form['Profile'] = load_file("victim.jpg")
    os.remove("victim.jpg")
    print("कृपया विवरण बताएं ।\nघटना की तिथि ।")
    speak("कृपया विवरण बताएं ।\nघटना की तिथि ।")
    form["Date_of_incident"] = takecommand()
    print('घटना का स्थान।')
    speak('घटना का स्थान।')
    form['Place_pf_incident'] = takecommand()
    print('कृपया पूरा विवरण दें।')
    speak('कृपया पूरा विवरण दें।')
    form['Description'] = takecommand()

    form["Victim_Name"] = form.pop("Name")
    form['Investigating_officer'] = str(db.min_case_off())
    db.fir_register(form)
    send.send_message()
    print("सभी विवरण सफलतापूर्वक भेजे गए हैं।")
    speak("All the details has been send successfully.")


