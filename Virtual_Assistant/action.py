import Text_to_speech
import Speech_to_text
import datetime
import webbrowser

user_data = Speech_to_text.speech_to_text()

if "What is your name" in user_data:
    Text_to_speech.text_to_speech()
    print("My name is Virtual Assistant.")
elif "How are you" in user_data:
    Text_to_speech.text_to_speech()
    print("I am fine, thank you. How can I assist you today?")
elif "What time is it" in user_data:
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    Text_to_speech.text_to_speech()
    print("The current time is " + current_time)
elif "Open YouTube" in user_data:
    Text_to_speech.text_to_speech()
    print("Opening YouTube")
    webbrowser.open("https://www.youtube.com")
elif "Open Google" in user_data:
    Text_to_speech.text_to_speech()
    print("Opening Google")
    webbrowser.open("https://www.google.com")
elif "Open Gmail" in user_data:
    Text_to_speech.text_to_speech()
    print("Opening Gmail")
    webbrowser.open("https://mail.google.com")
else:
    Text_to_speech.text_to_speech()
    print("I am sorry, I did not understand that command.")