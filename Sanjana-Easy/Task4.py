import pyaudio
import wave

FRAMES__PER_BUFFER=3200
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000

p=pyaudio.PyAudio()

stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=TRUE,frames_per_buffer=FRAMES__PER_BUFFER)

print("start recoring")

seconds=5
frames=[]
for i in range(0,int(RATE/FRAMES__PER_BUFFER*seconds)):
    data=stream.read(FRAMES__PER_BUFFER)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

obj=wave.open("recording.wave","wb")
obj.setnchannels(CHANNELS)
obj.setsampwidth(p.get_sample_size(FORMAT))
obj.setframerate(RATE)
obj.writeframes(b"".join(frames))
obj.close()