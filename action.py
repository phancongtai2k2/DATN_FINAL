from time import sleep
from IR_Sensor.IR import IRSensor
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from DC.MotorControl import MotorControl
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def activate_DC(predict):
    try:
        factory = PiGPIOFactory()
        servo_door = Servo(16, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)   #chan vat ly 36
        rotate_motor = MotorControl(in1 = 22 ,in2 = 27 ,ena = 17 )  # tuong ung chan vat ly 15 , 13 , 11
        
        #glass
        if(predict == 0):
            read_ir_glass = IRSensor(pin = 26) #Chan vat ly 37
            
            while(True):
                rotate_motor.backward() # nguoc chieu kim dong ho
                rotate_motor.setSpeed(50)   # dieu chinh toc do
                rg = read_ir_glass.read_sensor()
                if(rg == 1):
                    rotate_motor.stop()
                    break
            print('Open door')
            sleep(1)
            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(3)
            servo_door.mid()
            sleep(0.5)
            print('Close door')
            
            read_ir_pet = IRSensor(pin = 6) # chan vat ly 31
            
            while(True):
                rotate_motor.forward() # thuan chieu kim dong ho
                rotate_motor.setSpeed(50)
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    rotate_motor.stop()
                    break
        #hdpe
        elif(predict == 1):
            read_ir_hdpe = IRSensor(pin = 19)    # chan vat ly 35
            
            while(True):
                rotate_motor.backward() # nguoc chieu kim dong ho
                rotate_motor.setSpeed(50)   # dieu chinh toc do
                rh = read_ir_hdpe.read_sensor()
                if(rh == 1):
                    rotate_motor.stop()
                    break
            print('Open door')
            sleep(1)
            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(3)
            servo_door.mid()
            sleep(0.5)
            print('Close door')

            read_ir_pet = IRSensor(pin = 6) # chan vat ly 31
            
            while(True):
                rotate_motor.forward()  # thuan chieu kim dong ho
                rotate_motor.setSpeed(50) # dieu chinh toc do
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    rotate_motor.stop()
                    break
        #metal
        elif(predict == 2):
            read_ir_metal = IRSensor(pin = 13) #chan vat ly 33
            
            while(True):
                rotate_motor.forward() # thuan chieu kim dong ho
                rotate_motor.setSpeed(50)
                rm = read_ir_metal.read_sensor()
                if(rm == 1):
                    rotate_motor.stop()
                    break
            print('Open door')
            sleep(1)
            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(3)
            servo_door.mid()
            sleep(0.5)
            print('Close door')

            read_ir_pet = IRSensor(pin = 6) # chan vat ly 31
            
            while(True):
                rotate_motor.backward() # nguoc chieu kim dong ho
                rotate_motor.setSpeed(50)
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    rotate_motor.stop()
                    break
        #pet
        elif(predict == 3):
            read_ir_pet = IRSensor(pin = 6)   # chan vat ly 31
            
            while(True): 
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    break 
                elif(rp == 0):
                    while(True):
                        rotate_motor.forward() # thuan chieu kim dong ho
                        rotate_motor.setSpeed(50)
                        rp = read_ir_pet.read_sensor()
                        if(rp == 1):
                            rotate_motor.stop() 
                            break
                    break

            print('Open door')
            sleep(1)
            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(3)
            servo_door.mid()
            sleep(0.5)
            print('Close door')
                  
    finally:
        GPIO.cleanup()            

