
from gtts import gTTS
from playsound import playsound
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




def speak(query):
    audio_created = gTTS(text=query, lang="hi", slow=False)
    audio_created.save("my_file.mp3")
    playsound('my_file.mp3')
    os.remove('my_file.mp3')


def welcome():
    # it give us the hour in 0 to 24
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        print("शुभ प्रभात । \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
    elif hour >= 12 and hour < 16:
        print("नमस्कार। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
    elif hour >= 16 and hour < 20:
        print("सुसंध्या। \nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")
    else:
        print("घबराइए मत हम आपकी मदद करने के लिए यहां हैं।\nस्मार्ट पुलिस स्टेशन में आपका स्वागत है ।\nमैं आपका सहायक जारा हूं। मैं यहाँ आप की सहायता हेतु हूँ।\nकृपया अपना आधार कार्ड नंबर दर्ज करें।")

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
    form=db.adhaar(number)
    for i in form.keys():
        if i == 'Name':
            temp = translator.translate(text=str(i)+": "+str(form[i]), dest='hi', src='en').text
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



    print("Please put your thumb in fingure print scanner.")
    print("Please wait verification is in process.")

    tryy = 3
    while not verify.fingure(form["Adhaar_no"]):
        print("Fingure print did not verified please try again after cleaning your fingure.\nYou have only {} chance left.".format(tryy))
        tryy = tryy - 1
        if tryy:
            pass
        else:
            print("You exceed maximum number of attempt.")
            sys.exit()
    else:
        print("Fingure print succesesfully verified")

    print("Please be infront of the camera.")
    tryy=3
    while not face_capture.capture():
        print("Face did not recognized please try again after removing all obsticle from the face. Face should be clearly in front of camera.")
        tryy=tryy-1
        if tryy:
            pass
        else:
            print(" You exceed maximum number of attempt.")
            sys.exit()
    else:
        print("Face has been sucessfully captured")

    form['Profile'] = load_file("victim.jpg")
    os.remove("victim.jpg")
    print("कृपया विवरण बताएं ।\nघटना की तिथि ।")
    form["Date_of_incident"] = input()
    print('घटना का स्थान।')
    form['Place_pf_incident'] =input()
    print('कृपया पूरा विवरण दें।')
    form['Description'] = input()

    form["Victim_Name"] = form.pop("Name")
    form['Investigating_officer'] = str(db.min_case_off())
    db.fir_register(form)
    send.send_message()
    print("सभी विवरण सफलतापूर्वक भेजे गए हैं")


