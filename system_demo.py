from ultralytics import YOLO
import random
from detect_by_Yolo import detect_yolov8
#sensorHCSR
from gpiozero import DistanceSensor, AngularServo
from time import sleep

#initRecord 
from cut_audio import cut_Audio

#Audio
from predict_audio import predict_audio_def, record_audio
import argparse

from action import activate_DC

# initGPIO_HCSR , chan vat ly 16 va 18
sensor = DistanceSensor(echo = 23, trigger = 24)

#init servo GPIO 17, chan vat ly 11
servo_door = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)

#init servo GPIO 18, chan vat ly 12
servo_knock = AngularServo(18, min_pulse_width=0.0006, max_pulse_width=0.0023)

#init modelYOLO
model = YOLO("models\last.pt")

#read_hcsr
# def read_hcsr():
#     s = sensor.distance 
#     return s

if __name__ == "__main__":
    
    while(True):

        # print("Open Yolo vs Led\n")
        # led = 1     # bat led 
        # print("bat den led cung cap anh sang!\n")
        # detect_yolov8()

        print("Open Audio")
        audio_path = "save_record_audio/audio_save.wav"
        record_audio(audio_path, 5)       #duong dan save file record, 5s
        output_file_path = "save_record_audio_new/audio_save.wav"
        cut_Audio(audio_path,output_file_path)               #cắt xong ghi đè lên file audio_save
        
        #predict_audio
        t = predict_audio_def(output_file_path)
        
        activate_DC(t , servo_door)

        sleep(10)
            

            


            






