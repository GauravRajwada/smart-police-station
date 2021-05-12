from New_Case import eng_assistant, hin_assistant, Hindi, English
import athority
import databse as db

if __name__ == '__main__':
    hindi_welcome = 'स्मार्ट पुलिस स्टेशन में आपका स्वागत है।\nहिंदी में जारी रखने के लिए कृपया 2 दबाएँ'
    english_welcome = "welcome to Smart Police Station\nTo continue in English please press 1"
    print(english_welcome)
    eng_assistant.speak(english_welcome)
    print(hindi_welcome)
    hin_assistant.speak(hindi_welcome)
    choice=int(input())
    if choice==2:
        print("क्या आपको असिस्टेंट चाहिए तो एक दबाए नहीं तो दो दबाये")
        hin_assistant.speak("कक्या आपको असिस्टेंट चाहिए तो एक दबाए नहीं तो दो दबाये")
        n=int(input())
        if n==1:
            hin_assistant.main()
        else:
            Hindi.main()
    else:
        print("If you want assistant then press 1 otherwise press 2.")
        eng_assistant.speak("If you want assistant then press 1 otherwise press 2.")
        n=int(input())
        if n==1:
            eng_assistant.main()
        else:
            English.main()
    athority.notify(db.recent_case())
