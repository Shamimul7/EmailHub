import smtplib
import speech_recognition as sagor
import pyttsx3
from email.message import EmailMessage

listener = sagor.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sagor.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('msdvk385@gmail.com', 'msdhoni7')
    email = EmailMessage()
    email['From'] = 'msdvk385@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'boss': 'emtiaz15-8877@diu.edu.bd',
    'wife': 'tasminnishu@gmail.com',
    'faisal': 'faisal15-9314@diu.edu.bd'
}


def get_email_info():
    talk('Please Choose Email Receiver')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('Tell Me The Subject')
    subject = get_info()
    talk('Tell Me The Message')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey Boss! Your Email Is Sent Successfully')
    talk('Do You Want To Send Another Email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()