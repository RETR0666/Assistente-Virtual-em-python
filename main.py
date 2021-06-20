import speech_recognition as sr


def recognizer():
    rec = sr.Recognizer()

    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)

        while True:
            audio = rec.listen(source)
            inputAudio = rec.recognize_google(audio, language="pt-br")
            return str(inputAudio)


speech = sr.Recognizer()
print(speech)
