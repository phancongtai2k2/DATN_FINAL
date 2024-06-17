from HCSR04.read_distance import measure_distance
from action import activate_DC
from detect_by_Yolo import detect_yolov8

from time import sleep
from IR_Sensor.IR import IRSensor
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from DC.MotorControl import MotorControl
import RPi.GPIO as GPIO

factory = PiGPIOFactory()
servo_knock = Servo(20, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)   #chan vat ly 38
print('Open door')
sleep(0.1)
servo_knock.min()   #Thay doi phu hop voi cach dat servo
sleep(0.3)
servo_knock.mid()
sleep(0.5)
print('Close door')

#measure_distance()
#i=detect_yolov8()
#activate_DC(1)

