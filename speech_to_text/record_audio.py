import sounddevice as sd
import wave
import os

def record_audio(filename="audio_samples/example.wav", duration=5, samplerate=16000):
    os.makedirs("audio_samples", exist_ok=True)
    print(f"🎙️ Recording for {duration} seconds... Speak now.")

    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(recording.tobytes())

    print(f"✅ Saved to {filename}")

if __name__ == "__main__":
    record_audio()
