from HCSR04.read_distance import measure_distance
from action import activate_DC
#from detect_by_Yolo import detect_yolov8
from detect_by_Yolo import detect_yolov8
from Relay_LED.test_relay import turn_on
from Relay_LED.test_relay import turn_off
from time import sleep

# from time import sleep
# from IR_Sensor.IR import IRSensor
# from gpiozero import Servo
# from gpiozero.pins.pigpio import PiGPIOFactory
# from DC.MotorControl import MotorControl
# import RPi.GPIO as GPIO




# measure_distance() 

# factory = PiGPIOFactory()
# servo_knock = Servo(20, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)   #chan vat ly 38
# while(True):
#      print('Open knock')
#      sleep(0.1)
#      servo_knock.min()   #Thay doi phu hop voi cach dat servo
#      sleep(3)
#      servo_knock.max()
#      sleep(0.5)
#      print('Close knock')
#      sleep(1.5)
#      print("Finally")
#      print("")
turn_off(2)


while(True):
   measure_distance() 
   turn_on(2)
   sleep(1)
   i = detect_yolov8()
   sleep(1)
   activate_DC(i)
   turn_off(2)

