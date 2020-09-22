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