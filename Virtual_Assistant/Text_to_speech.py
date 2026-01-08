import pyttsx3

def text_to_speech():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)  
    engine.say("Hello, I am your virtual assistant. How can I help you today?")
    engine.runAndWait()