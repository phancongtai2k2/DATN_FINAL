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
        servo_door = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)   #chan vat ly 11
        rotate_motor = MotorControl(in1 = 27 ,in2 = 22 ,ena = 14 )  # tuong ung chan vat ly 13 , 15 , 8
        
        #glass
        if(predict == 0):
            
            # read_ir_glass = IRSensor(pin = 5) # chan vat ly 29
            print("0 ")    

            while(True):
                rotate_motor.backward() # nguoc chieu kim dong ho
                rotate_motor.setSpeed(60)   # dieu chinh toc do dong co
                read_ir_glass = IRSensor(pin = 5) 
                rg = read_ir_glass.read_sensor()
                if(rg == 1):
                    rotate_motor.stop()
                    break

            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(1)
            servo_door.mid()
            
            read_ir_pet = IRSensor(pin = 26) # chan vat ly 37
            
            while(True):
                rotate_motor.forward() # thuan chieu kim dong ho
                rotate_motor.setSpeed(60)
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    rotate_motor.stop()
                    break
        #hdpe
        elif(predict == 1):
            read_ir_hdpe = IRSensor(pin = 6)    # chan vat ly 31
            
            while(True):
                rotate_motor.forward()  # thuan chieu kim dong ho
                rotate_motor.setSpeed(90)
                rh = read_ir_hdpe.read_sensor()
                if(rh == 1):
                    rotate_motor.stop()
                    break
            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(1)
            servo_door.mid()

            read_ir_pet = IRSensor(pin = 26) # chan vat ly 37
            
            while(True):
                rotate_motor.forward() #thuan chieu kim dong ho
                rotate_motor.setSpeed(90)
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    rotate_motor.stop()
                    break
        #metal
        elif(predict == 2):
            read_ir_metal = IRSensor(pin = 16) #chan vat ly 36
            
            while(True):
                rotate_motor.forward() # thuan chieu kim dong ho
                rotate_motor.setSpeed(60)
                rm = read_ir_metal.read_sensor()
                if(rm == 1):
                    rotate_motor.stop()
                    break
            servo_door.min()   #Thay doi phu hop voi cach dat servo
            sleep(1)
            servo_door.mid()

            read_ir_pet = IRSensor(pin = 26) # chan vat ly 37
            
            while(True):
                rotate_motor.backward() # nguoc chieu kim dong ho
                rotate_motor.setSpeed(60)
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    rotate_motor.stop()
                    break
        #pet
        elif(predict == 3):
            read_ir_pet = IRSensor(pin = 26 )   # chan vat ly 37
            
            while(True): 
                rp = read_ir_pet.read_sensor()
                if(rp == 1):
                    servo_door.min()   #Thay doi phu hop voi cach dat servo
                    sleep(1)
                    servo_door.mid() 
                else:
                    while(True):
                        rotate_motor.forward() # thuan chieu kim dong ho
                        rotate_motor.setSpeed(90)
                        rp = read_ir_pet.read_sensor()
                        if(rp == 1):
                            rotate_motor.stop()
                        break
                break
    finally:
        GPIO.cleanup()            

activate_DC( predict=0 )