import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary
import requests
import openai
# import google.generativeai as genai

import time
import asyncio
import edge_tts


# genai.configure(api_key="AIzaSyC0YPn6sFaBzBVgJaKpltQGUng21AF_Dvg")  

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "b09023694bc539db012a7234eaec45d6"

# Text-to-Speech
# def speak(text):
#     engine.say(text)
#     engine.runAndWait()
def speak(text):
    asyncio.run(_speak(text))

async def _speak(text):
    communicate = edge_tts.Communicate(text, voice="en-IN-PrabhatNeural")
    await communicate.save("output.mp3")
    import playsound
    playsound.playsound("output.mp3")

# AI Chat via local OpenAI API
def aiChat(input):
    openai.api_base = 'http://localhost:11434/v1'
    openai.api_key = 'sk-ollama'  # dummy key
    response = openai.ChatCompletion.create(
        model="tinyllama",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named jarvis created by shyam, please response in short replies."},
            {"role": "user", "content": input}
        ],
        temperature=0,
        max_tokens=100
    )
    return response['choices'][0]['message']['content']



# Handle Commands
def processCommand(command):    
    command = command.lower()
    if "hello" in command:
        speak("Hello Shyam! How can I help you?")
    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif "open twitter" in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif command.startswith("play"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            link = musicLibrary.music.get(song)
            if link:
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak("Sorry, I couldn't find that song.")
        else:
            speak("Please say the song name after 'play'.")
    elif "news" in command:
        speak("Fetching the latest news...")
        r = requests.get(f"https://gnews.io/api/v4/top-headlines?country=in&lang=en&token={newsapi}")
        if r.status_code == 200:
            articles = r.json().get("articles", [])
            for article in articles[:5]:  # Only top 5 headlines
                speak(article["title"])
                time.sleep(1.5)  # Delay between news
        else:
            speak("Failed to fetch news.")
    else:
        # print("Query to AI:", command)
        output = aiChat(command)
        print("AI says:", output)
        speak(output)

# Main Jarvis loop
if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            try:
                word = recognizer.recognize_google(audio)
                print(f"Detected: {word}")

                if "jarvis" in word.lower():
                    speak("Welcome Shyam, how can I assist you?")
                    time.sleep(0.5)

                    while True:
                        with sr.Microphone() as source:
                            print("Listening for command...")
                            recognizer.adjust_for_ambient_noise(source, duration=0.5)
                            try:
                                command_audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
                                command = recognizer.recognize_google(command_audio)
                                print("Command:", command)

                                if any(exit_word in command.lower() for exit_word in ["exit", "quit", "stop", "goodbye", "go to sleep"]):
                                    speak("Okay, going back to sleep.")
                                    break

                                processCommand(command)
                            except sr.UnknownValueError:
                                speak("Sorry, I didn't catch that. Please repeat.")
                            except sr.RequestError as e:
                                speak(f"Speech recognition error: {e}")


            except sr.UnknownValueError:
                print("Could not understand audio.")
            except sr.RequestError as e:
                print(f"Speech service error: {e}")
            except Exception as e:
                print(f"General Error: {e}")

        except KeyboardInterrupt:
            print("\n[INFO] Exiting gracefully.")
            speak("Shutting down Jarvis.")
            break
