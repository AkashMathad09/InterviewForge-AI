import speech_recognition as sr


def listen_answer():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak your answer...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print("\nRecognized Answer:")
        print(text)

        return text

    except sr.UnknownValueError:
        print("Speech not understood")
        return ""

    except sr.RequestError:
        print("Speech service error")
        return ""