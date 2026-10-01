import os
import pyttsx3
import speech_recognition as sr
import PyPDF2


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)
    print(text)
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query

    except Exception:
        speak("Please say that again.")
        return "None"


def read_book():
    speak("Please enter the path of the PDF file, including its name.")
    file_path = input("Enter the PDF file path: ")

    try:
        if not os.path.exists(file_path):
            speak("Sorry, the PDF file was not found.")
            return

        with open(file_path, "rb") as book:
            pdf_reader = PyPDF2.PdfReader(book)
            total_pages = len(pdf_reader.pages)

            speak(f"The book contains {total_pages} pages.")
            print(f"Total pages: {total_pages}")

            speak("Which page should I start reading from?")
            page_number = int(input("Enter the page number: "))

            if page_number < 1 or page_number > total_pages:
                speak(f"Please enter a page number between 1 and {total_pages}.")
                return

            page = pdf_reader.pages[page_number - 1]
            text = page.extract_text()

            if text:
                speak(text)
            else:
                speak("Sorry, I could not extract any text from this page.")

    except ValueError:
        speak("Please enter a valid page number.")

    except Exception as e:
        print(f"Error: {e}")
        speak("Sorry, I was unable to read the PDF file.")


read_book()
