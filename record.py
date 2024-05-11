import pyaudio
import wave

def record_audio(output_filename, duration=5, sr=44100, chunk=1024, format=pyaudio.paInt16, channels=1):
    p = pyaudio.PyAudio()

    stream = p.open(format=format,
                    channels=channels,
                    rate=sr,
                    input=True,
                    frames_per_buffer=chunk)

    print("* Recording audio...")

    frames = []

    for _ in range(0, int(sr / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("* Done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sr)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    output_filename = "recorded_audio2.wav"
    duration = 5  # in seconds

    record_audio(output_filename, duration)
