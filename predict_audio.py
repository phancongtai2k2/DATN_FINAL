import pyaudio
import wave
import numpy as np
from tensorflow.keras.models import load_model
from clean import downsample_mono, envelope
from kapre.time_frequency import STFT, Magnitude, ApplyFilterbank, MagnitudeToDecibel
import argparse
import os

def record_audio(output_filename, duration=5, sr=16000):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = sr
    RECORD_SECONDS = duration
    
    p = pyaudio.PyAudio()
    
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* Recording audio...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* Done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def load_and_predict(audio_file, model):
    rate, wav = downsample_mono(audio_file, sr=16000)
    mask, env = envelope(wav, rate, threshold=20)
    clean_wav = wav[mask]
    step = int(16000*1.0)
    batch = []

    for i in range(0, clean_wav.shape[0], step):
        sample = clean_wav[i:i+step]
        sample = sample.reshape(-1, 1)
        if sample.shape[0] < step:
            tmp = np.zeros(shape=(step, 1), dtype=np.float32)
            tmp[:sample.shape[0],:] = sample.flatten().reshape(-1, 1)
            sample = tmp
        batch.append(sample)
    X_batch = np.array(batch, dtype=np.float32)
    y_pred = model.predict(X_batch)
    y_mean = np.mean(y_pred, axis=0)
    y_pred = np.argmax(y_mean)
    return y_pred

def predict_audio_def(path_save_audio):
    parser = argparse.ArgumentParser(description="Record audio and make prediction")
    parser.add_argument("--model_fn", type=str, default="models/lstm.h5", help="Path to the model file")
    args = parser.parse_args()

    model = load_model(args.model_fn,
        custom_objects={'STFT':STFT,
                        'Magnitude':Magnitude,
                        'ApplyFilterbank':ApplyFilterbank,
                        'MagnitudeToDecibel':MagnitudeToDecibel},
                        compile=False)

    # # Record audio
    # audio_filename = "save.wav"
    # record_audio(audio_filename)

    # Make prediction
    prediction = load_and_predict(path_save_audio, model)

    if prediction == 0:
        print("Predicted class: Glass_0")
    elif prediction == 1:
        print("Predicted class: HDPE_1")
    elif prediction == 2:
        print("Predicted class: METAL_2")
    elif prediction == 3:
        print("Predicted class: PET_3")
    else:
        print("ERROR")
    
    return prediction
