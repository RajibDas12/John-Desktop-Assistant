import pyttsx3
import speech_recognition as sr
import wikipedia

speaker = pyttsx3.init('sapi5')
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[0].id)


def speakwithme(audio):
    speaker.say(audio)
    speaker.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speakwithme("Good Morning! ")

    elif hour >= 12 and hour < 17:
        speakwithme("Good Afternoon! ")

    elif hour >= 17 and hour < 19:
        speakwithme("Good Evening! ")

    else:
        speakwithme("Good Night! ")
    speakwithme("I am your  Vertual  Assistant John. Please tell me how may I help you")


def takeCmd():
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        reco.pause_threshold = 1
        audio = reco.listen(source)

    try:
        print("Recognizing...")
        askedme = reco.recognize_google(audio, language='en-in')
        print(f"User said: {askedme}\n")

    except Exception as e:
        print("Say that again please...")
        speakwithme("Connection error")
        return "None"
    return askedme


if __name__ == "__main__":
    wishMe()
    while True:
        askedme = takeCmd().lower()

        if 'wikipedia' in askedme:
            speakwithme('Searching Wikipedia...')
            askedme = askedme.replace("wikipedia", "")
            results = wikipedia.summary(askedme, sentences=2)
            speakwithme("According to Wikipedia")
            speakwithme(results)

        elif "who are you" in askedme or "about you" in askedme or "your details" in askedme:
            who_you = "I am John an A I based computer program !"
            print(who_you)
            speakwithme(who_you)

        elif 'good bye' in askedme:
            speakwithme("good bye")
            exit()

        elif "your name" in askedme or "sweat name" in askedme:
            na_me = "Thanks for Asking my self ! John"
            print(na_me)
            speakwithme(na_me)

        elif "you feeling" in askedme:
            speakwithme("feeling Very happy to help you")

        elif "shutdown" in askedme:
            speakwithme("shutting down")
            os.system('shutdown -s')

        elif 'the time' in askedme:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speakwithme(f"the time is {strTime}")

        elif 'open youtube' in askedme:
            webbrowser.open("www.youtube.com")
            speakwithme("opening youtube")

        elif 'open github' in askedme:
            webbrowser.open("https://www.github.com")
            speakwithme("opening github")

        elif 'open facebook' in askedme:
            webbrowser.open("https://www.facebook.com")
            speakwithme("opening facebook")

        elif 'open instagram' in askedme:
            webbrowser.open("https://www.instagram.com")
            speakwithme("opening instagram")

        elif 'open google' in askedme:
            webbrowser.open("google.com")
            speakwithme("opening google")

        elif 'open yahoo' in askedme:
            webbrowser.open("https://www.yahoo.com")
            speakwithme("opening yahoo")

        elif 'open gmail' in askedme:
            webbrowser.open("https://mail.google.com")
            speakwithme("opening google mail")

        elif 'open snapdeal' in askedme:
            webbrowser.open("https://www.snapdeal.com")
            speakwithme("opening snapdeal")

        elif 'open amazon' in askedme:
            webbrowser.open("https://www.amazon.com")
            speakwithme("opening amazon")

        elif 'open flipkart' in askedme:
            webbrowser.open("https://www.flipkart.com")
            speakwithme("opening flipkart")

        elif 'how are you' in askedme:
            setMsgme = ['Just doing my thing!', 'I am fine!', 'Nice!']
            ans_q = random.choice(setMsgme)
            speakwithme(ans_q)
            speakwithme(" How are you'")
            ans_how_are_you = takeCmd()
            if 'fine' in ans_how_are_you or 'happy' in ans_how_are_you or 'okey' in ans_how_are_you:
                speakwithme('Great')
            elif 'not' in ans_how_are_you or 'sad' in ans_how_are_you or 'upset' in ans_how_are_you:
                speakwithme('Tell me how can i make you happy')
            else:
                speakwithme("I can't understand. Please say that again !")

        elif askedme == 'none':
            continue

        elif 'exit' in askedme or 'stop' in askedme or 'quit' in askedme:
            exx_exit = 'See you soon. Bye'
            speakwithme(exx_exit)
            exit()

        else:
            tempp = askedme.replace(' ', '+')
            ur_url = "https://www.google.com/search?q="
            res_p = 'sorry! i cant understand but i search from internet to give your answer !'
            speakwithme(res_p)
            webbrowser.open(ur_url + tempp)