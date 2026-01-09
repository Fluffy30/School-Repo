from tkinter import Tk, LabelFrame, Label, Text, Entry, Button, SOLID
from PIL import Image, ImageTk
import action
import Speech_to_text

root = Tk()
root.title("Ai Assistant")
root.geometry("550x675")
root.configure(bg="#2C3E50")    
root.resizable(False, False)
root.config(bg="#2C3E50")

#ask

def ask():
    ask_val= Speech_to_text.speech_to_text()
    bot_val= action.action(ask_val)
    text.insert('End', "You: " + ask_val + '\n')
    if bot_val != "None":
        text.insert('End', "Bot: " + str(bot_val) + '\n')
    if bot_val == "Okay Sir":
        root.destroy()

#send

def send():
    send = entry.get()
    bot = action.action(send)
    text.insert('End', "You: " + send + '\n')
    if bot != "None":
        text.insert('End', "Bot: " + str(bot) + '\n')
    if bot == "Okay Sir":
         root.destroy()

#delete

def delete():
    text.delete('1.0', 'end')

#frame

frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.configure(bg="#34495E")
frame.grid(row=0, column=1, padx=55, pady=10)

#text label

text_label = Label(frame, text="AI Assistant", font=("Helvetica", 24, "bold"), bg="#2C3E50")
text_label.grid(row=0, column=0 , padx=20, pady=10)

#Image

#image = ImageTk.PhotoImage(Image.open("C:\\Users\\ADMIN\\OneDrive\\Desktop\\Brown\\School-Repo\\Virtual_Assistant\\siri.png"))
#image_label = Label(frame, image=image)
#image_label.grid(row=1, column=0, pady=20)

#Adding Text Label

text = Text(root, font=("Helvetica", 14), bg="#2C3E50")
text.grid(row=2, column=0)
text.place(x=100, y=375, width=375, height=100)

#Entry Box

entry = Entry(root, justify="center")
entry.place(x=100, y=500, width=350, height=30)

#button 1

Button1 = Button(root, text="Ask", bg="#34495E", pady=16, padx=40, borderwidth=3, relief=SOLID, command= ask)
Button1.place(x=70, y=575)

#button 2

Button2 = Button(root, text="Send", bg="#34495E", pady=16, padx=40, borderwidth=3, relief=SOLID, command= send)
Button2.place(x=400, y=575)

#button 3

Button3 = Button(root, text="Delete", bg="#34495E",pady=16, padx=40, borderwidth=3, relief=SOLID, command= delete)
Button3.place(x=225, y=575)

root.mainloop()
