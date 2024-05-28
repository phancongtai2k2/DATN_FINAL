from ultralytics import YOLO
import random
from detect_by_Yolo import detect_yolov8

#sensorHCSR
from gpiozero import DistanceSensor
from time import sleep

#initRecord 
from record import record_audio
from cut_audio import cut_Audio

#Audio
from predict_audio import predict_audio_def
import argparse

#initGPIO_HCSR
sensor = DistanceSensor(echo = 23, trigger = 24)

#init modelYOLO
model = YOLO(r"/home/pi/DATN_FINAL/models/last.pt")

#read_hcsr
def read_hcsr():
    s = sensor.distance 
    return s

if __name__ == "__main__":
    while(1):
        #d = read_hcsr()
        d = random.randint(0,20)

        led = 0 #khoi tao gia tri led = 0 sau moi lan 

        if(d < 10):     #10 la khoang cach khong co vat
            print("Open Yolo vs Led\n")
            led = 1     # bat led 
            print("bat den led cung cap anh sang!\n")
            detect_yolov8()

            print("Open Audio")
            audio_path = "save_record_audio/audio_save.wav"
            record_audio(audio_path, 5 )       #duong dan save file record, 5s
            output_file_path = "save_record_audio_new/audio_save.wav"
            cut_Audio(audio_path,output_file_path)               #cắt xong ghi đè lên file audio_save

            #predict_audio
            predict_audio_def(output_file_path)
            print('Xong tien trinh')
        sleep(10)
        
            

            


            






