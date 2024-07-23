import pyaudio
import wave
from pydub import AudioSegment

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def record_audio(seconds, filename):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=FRAMES_PER_BUFFER)
    print("Start recording")
    frames = [stream.read(FRAMES_PER_BUFFER) for _ in range(int(RATE / FRAMES_PER_BUFFER * seconds))]
    print("Recording finished")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def playback_audio(filename):
    with wave.open(filename, 'rb') as wf:
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(), output=True)
        data = wf.readframes(FRAMES_PER_BUFFER)
        while data:
            stream.write(data)
            data = wf.readframes(FRAMES_PER_BUFFER)
        stream.stop_stream()
        stream.close()
        p.terminate()

def convert_format(input_filename, output_filename):
    audio = AudioSegment.from_wav(input_filename)
    audio.export(output_filename, format=output_filename.split('.')[-1])
    print(f"Recording saved as {output_filename}")

def main():
    actions = {
        '1': ('Record Audio', lambda: record_audio(int(input("Enter duration of recording in seconds: ")), input("Enter filename to save (with .wav extension): "))),
        '2': ('Playback Audio', lambda: playback_audio(input("Enter filename to playback (with .wav extension): "))),
        '3': ('Save Audio in Different Format', lambda: convert_format(input("Enter the recorded filename (with .wav extension): "), input("Enter the new filename with desired extension (e.g., recording.mp3): "))),
        '4': ('Exit', lambda: exit())
    }
    while True:
        print("\nVoice Recording Application")
        for key, (desc, _) in actions.items():
            print(f"{key}. {desc}")
        choice = input("Select an option: ")
        action = actions.get(choice)
        if action:
            action[1]()
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
