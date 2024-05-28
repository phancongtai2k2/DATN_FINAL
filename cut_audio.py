import librosa
from pydub import AudioSegment

def extract_audio_segment(input_file, start_time_s):
    # Đọc tệp âm thanh vào
    audio = AudioSegment.from_wav(input_file)
        
    # Chuyển đổi thời gian từ giây sang mili giây
    start_time_ms = start_time_s * 1000
    end_time_ms = start_time_ms + 500
    
    # Trích xuất đoạn âm thanh
    extracted_segment = audio[start_time_ms:end_time_ms]
    
    return extracted_segment

def get_start_time(sp):
    global start_time
    for j in range (len(sp)):
        if sp[j] > 0.5:
            start_time = int(j/16000)
            break
    return start_time
def cut_Audio(input_audio_path,output_file_path):
    samples, sample_rate = librosa.load(input_audio_path, sr = 16000)
    j = 0
    while j < len(samples) - sample_rate:
        if samples[j] > 0.3:
            st = (j/sample_rate)
            extracted_audio = extract_audio_segment(input_audio_path, st)
            extracted_audio.export(output_file_path, format= "wav")
        else:
            j = j + 1