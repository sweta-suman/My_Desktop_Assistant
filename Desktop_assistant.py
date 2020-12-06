import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
engine= pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am shweta's assistant,please tell me how can i help you")
def takecommand():
    """it takes microphone voice as input and returns string object"""
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING !!! wait for a while")
        r.pause_threshold=3
        audio=r.listen(source)
    try:
        print("Recognising...")
        query=r.recognize_google(audio,language='en-in')
        print("User said:\n",query)
    except Exceptions as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query
    
if __name__=='__main__':
    wishMe()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("HOLD ON .....Searching wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "youtube" in query:
            webbrowser.open("youtube.com")
        elif "google" in query:
            webbrowser.open("google.com")
        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
        elif "play music" in query:
            music_dir='C:\\Users\\hp\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,1)]))
        elif ' time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strtime}")
        elif 'visual code' in query:
            path="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif 'notepad' in query:
            path="C:\\WINDOWS\\system32"
            os.startfile(path)
        elif 'chrome' in query:
            webbrowser.open("chrome.com")
        elif 'turbo c ' in query:
            path="C:\\TURBOC3\\Turbo C++\\"
            os.startfile(path)
        elif 'quit' in query:
            break
print("thank you")       
                      
            
            
            
        
        
    
