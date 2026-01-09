import Text_to_speech
import Speech_to_text
import datetime
import webbrowser

def action(user_data):
    if "What is your name" in user_data:
        Text_to_speech.text_to_speech()
        return "My name is Virtual Assistant."
    elif "How are you" in user_data:
        Text_to_speech.text_to_speech()
        return "I am fine, thank you. How can I assist you today?"
    elif "What time is it" in user_data:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M")
        Text_to_speech.text_to_speech()
        return "The current time is " + current_time
    elif "Open YouTube" in user_data:
        Text_to_speech.text_to_speech()
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"
    elif "Open Google" in user_data:
        Text_to_speech.text_to_speech()
        webbrowser.open("https://www.google.com")
        return "Opening Google"
    elif "Open Gmail" in user_data:
        Text_to_speech.text_to_speech()
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"
    else:
        Text_to_speech.text_to_speech()
        return "I am sorry, I did not understand that command."