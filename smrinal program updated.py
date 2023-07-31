import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():   
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morninng!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am smrinal sir.Please tell me how may i help you")    
    
def takeCommand():
    #it takes microphone input from the user and returns strings output
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    
    except Exception as e:
        # print(e)
        
        print("Say that again please...")
        return "None"
    return query    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com','your-password-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()       
            
                 
    
if __name__ == "__main__":
    speak("Hi i am smrinal, memory 1 setupbite, 1 tb gigabyte superfast assisant with a cool voice,  feel youself lucky that you are using me")   
    wishMe()
    takeCommand()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia'in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            
        elif'open youtube' in query:
            webbrowser.open("youtube.com")
        elif'open youtube' in query:
            webbrowser.open("google.com")    
        elif'open stackeoverflow' in query:
            webbrowser.open("stackoverflow.com") 
        elif'open system setting' in query:
            webbrowser.open("system setting.com")       
        # elif 'play music' in query:    
        #     music_dir = 'D:\\Non Critical\\songs\\Favourite Songs2'
        #     songs = os.listeddir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        elif 'open code'in query:
            codePath = "C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codePath)
        elif'email to ronal' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "ronalyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ronal bhai. I am not able to send this email")   
        if 'quit' in query:
            exit()             
            
                