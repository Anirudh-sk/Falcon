import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import cv2
import time
import customtkinter
from PIL import Image, ImageTk
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from bs4 import BeautifulSoup
import googlesearch

# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()

def fetch_corpus(query):
    urls = url = next(googlesearch.search(query, num_results=5))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    corpus = []
    for tag in soup.find_all(['p', 'h1', 'h2', 'h3','h4']):
        corpus += tag.text + '\n'
    return corpus
    # corpus = []
    # # extract text from the HTML tags of each website
    # for url in urls:
    #     response = requests.get(url)
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     for tag in soup.find_all(['p', 'h1', 'h2', 'h3']):
    #         corpus += tag.text + '\n'
    # return corpus

def get_response(user_input, corpus):
    processed_input = user_input
    tfidf_vectorizer = TfidfVectorizer()
    tfidf = tfidf_vectorizer.fit_transform(corpus)
    tfidf_input = tfidf_vectorizer.transform([processed_input])
    similarity_scores = cosine_similarity(tfidf_input, tfidf)
    index = similarity_scores.argmax()
    return corpus[index]




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak (audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('hello there! good morning ')
    elif hour>=12 and hour<17:
        speak('hello there! good afternoon ')
    else :
        speak('hello there! good evening ')
    speak(" i am Falcon . How can i help you")

def microinput():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        print('listening....')
        # r.energy_threshold=700
        audio=r.listen(source)

    try:
        print('recognizing....')
        query=r.recognize_google(audio,language='en-in')
        print(f'user said : {query} \n')
        if 'yes' in query :
            speak('searching ....')
            print('searching....')

    except Exception as e:
        # print(e)
        time.sleep(5)
        speak('can you please speak up....')
        print('can you please speak up....')
        return "None"
    return query

def sendmail(to,content):
    server=smtplib.SMTP('smpt.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('amazinganirudhhere@gmail.com','password')
    server.sendmail('amazinganirudhhere@gmail.com',to,content)
    server.close()


def launch():
    greet()
    try:
        while True:
            query=microinput().lower()

            if 'youtube' in query:
                search=query.replace('youtube' and 'search for','')
                speak("opening youtube in browser")
                webbrowser.open(f'https://www.youtube.com/results?search_query={search}')

            elif 'open google' in query:
                speak("opening google in browser")
                webbrowser.open('www.google.com')

            elif 'spotify' in query or 'sportify' in query or 'spot if five' in query:
                search=query.replace('in spotify'and'play'and 'spotrtify' and 'spot if five','')
                speak("opening spotify in browser")
                webbrowser.open(f'https://open.spotify.com/search/{search}')

            elif 'open facebook' in query:
                speak("opening facebook in browser")
                webbrowser.open('www.facebook.com')


            elif 'open instagram' in query:
                speak("opening instagram in browser")
                webbrowser.open('www.instagram.com')

            elif 'open twitter' in query:
                speak("opening twitter in browser")
                webbrowser.open('www.twitter.com')

            elif 'open pinterest' in query:
                speak("opening pinterest in browser")
                webbrowser.open('www.pinterest.com')

            elif 'open github' in query:
                speak("opening github in browser")
                webbrowser.open('www.github.com')

            elif 'open gmail' in query:
                speak("opening gmail in browser")
                webbrowser.open('www.gmail.com')

            

            elif 'the time' in query:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f'the time is {time}')
                print(time)

            elif 'command prompt' in query:
                speak("opening command prompt")
                path="C:\\Windows\\system32\\cmd.exe"
                os.startfile(path)

            elif 'vs code' in query:
                speak("opening visual studio code")
                path="C:\\Program Files\\Microsoft VS Code\\code.exe"
                os.startfile(path)

            elif 'my computer' in query:
                speak("opening My computer")
                path="C:\\Users\\Anirudh\\Desktop"
                os.startfile(path)

            elif 'open pictures' in query:
                speak("opening pictures")
                path="C:\\Users\\Anirudh\\pictures"
                os.startfile(path)

            elif 'open videos' in query:
                speak("opening videos")
                path="C:\\Users\\Anirudh\\videos"
                os.startfile(path)

            elif 'open games' in query:
                speak("opening games")
                path="C:\\Users\\Anirudh\\saved games"
                os.startfile(path)

            elif 'open downloads' in query:
                speak("opening downloads")
                path="C:\\Users\\Anirudh\\Downloads"
                os.startfile(path)

            elif 'search' in query:
                statement=query.replace('search for', '')
                webbrowser.open(statement)

            elif 'shut down' in query or 'shutdown' in query:
                os.system('shutdown -s -t 10')
                
            elif 'restart' in query:
                os.system('shutdown -r -t 10')

            elif 'camera' in query:
                cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
                if not (cap.isOpened()):
                    speak('could not open camera')
                while(True):
                    ret,frame=cap.read()
                    cv2.imshow('Falcon Opened Camera',frame)
                    speak("Press Q to close the camera")
                    if cv2.waitKey(1)& 0xFF == ord('q'):
                        cap.release()
                        cv2.destroyAllWindows()
                        break
                # webbrowser.open(query)

            elif 'email' in query:
                speak("sending email")
                try:
                    speak('what should i mail ?')
                    content=microinput()
                    to='anirudhsk30@gmail.com'
                    sendmail(to,content)
                    speak('email sent successfully!!')
                except Exception as e:
                    print(e)
                    speak('unable to send email now !!')
                    print('email was not sent')

            elif "what\'s up" in query or 'how are you' in query:
                Msgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
                speak(random.choice(Msgs))

            elif 'news' in query:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                
            elif "your name"  in query:
                speak('my name is falcon')

            elif 'quit' in query or 'exit' in query or'go now' in query or'thank you' in query  :
                speak("have a great day!! if you want to call me again press the Talk to me Button")
                break

            elif 'wikipedia' in query :
                speak('searching wikipedia...')
                query=query.replace('wikipedia','')
                results=wikipedia.summary(query,sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)
            else : 
                corpus = fetch_corpus(query)
                corpus1=""
                corpus=corpus1.join(corpus)
                corpus = nltk.sent_tokenize(corpus)
                corpus = [sentence for sentence in corpus]           
                response = get_response(query, corpus)
                # print the response
                speak(response)
                print(response)
    except:
        speak("could not process the input can we try again click on Talk to me button to talk again")
        

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
# root.geometry("1000x1000")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frame, text="Falcon Your AI Assistant")
lable.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text='Talk to me', command=launch) # add command
button.pack(pady=12, padx=10)

image= ImageTk.PhotoImage(Image.open("./bot.png"))
button2 = customtkinter.CTkButton(master=frame, text="",  image=image) # add command
button2.pack(pady=12, padx=10)

root.mainloop()