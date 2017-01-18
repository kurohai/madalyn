import pyaudio,os
import speech_recognition as sr


def excel():
        os.system("start excel.exe")

def internet():
        os.system("start chrome.exe")

def media():
        os.system("start wmplayer.exe")

def mainfunction(source):
    print '1'

    audio = r.listen(source)
    print '2'
    
    user = r.recognize(audio)
    print '3'

    print(user)
    if user == "Excel":
        excel()
    elif user == "Internet":
        internet()
    elif user == "music":
        media()

if __name__ == "__main__":
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while 1:
            print 'hello'
            mainfunction(source)
