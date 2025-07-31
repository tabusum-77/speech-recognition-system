import speech_recognition as sr
import os

def transcribe_audio(file_path):
    print("File exists:", os.path.exists(file_path))  # DEBUG line
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            print("Transcription:", text)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"API Error: {e}")

if __name__ == "__main__":
    transcribe_audio(r"C:\Users\Shaik Mohammed Suhai\OneDrive\Desktop\speech_to_text\audio_samples\example_pcm.wav")
