import pyttsx3
tts_engine = pyttsx3.init()

test = 'alert 😂'

tts_engine.say(test)
tts_engine.runAndWait()