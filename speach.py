import speech_recognition as sr
import webbrowser

sr.microphone(device_index=1)
r=sr.recognizer()
r.energy_threshold=5000

with sr.microphone() as source:
    print("speek!")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("you said : {}",format(text))
        url='https://www.google.co.in/search?q='
        search_url=url+text
        webbrowser.open(search_url)
    except:
        print("can't recognize")
