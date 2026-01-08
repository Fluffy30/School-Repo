import speech_recognition as sr
import aifc

def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
      voice_data = ""
      voice_data = r.recognize_google(audio)
      print("You said: " + voice_data)
      return voice_data
    except sr.UnknownValueError:
       print("Sorry, I did not understand that.")
    except sr.RequestError:
       print("Sorry, my speech service is down.")