from time import sleep
from IR_Sensor.IR import IRSensor
from gpiozero import AngularServo
from DC.MotorControl import MotorControl
import RPi.GPIO as GPIO


def activate_DC(predict, servo_door):
    rotate_motor = MotorControl(in1 = 27 ,in2 = 22 ,ena = 14 )  # tuong ung chan vat ly 13 , 15 , 8
    GPIO.setmode(GPIO.BCM)
    #glass
    if(predict == 0):
        read_ir_glass = IRSensor(pin = 5) # chan vat ly 29
        while(True):
            rotate_motor.backward() # nguoc chieu kim dong ho
            rotate_motor.setSpeed(60)   # dieu chinh toc do dong co
            rg = read_ir_glass.read_sensor()
            if(rg == 1):
                rotate_motor.stop()
                break

        servo_door.angle = 90   #Thay doi phu hop voi cach dat servo
        sleep(1)
        servo_door.angle = -90
        
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
        servo_door.angle = 90   #Thay doi phu hop voi cach dat servo
        sleep(1)
        servo_door.angle = -90

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
        servo_door.angle = 90   #Thay doi phu hop voi cach dat servo
        sleep(1)
        servo_door.angle = -90

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
                servo_door.angle = 90   #Thay doi phu hop voi cach dat servo
                sleep(1)
                servo_door.angle = -90  
            else:
                while(True):
                    rotate_motor.forward() # thuan chieu kim dong ho
                    rotate_motor.setSpeed(90)
                    rp = read_ir_pet.read_sensor()
                    if(rp == 1):
                        rotate_motor.stop()
                    break
            break
                
servo_door = AngularServo(17, min_pulse_width=0.0006, max_pulse_width=0.0023)
activate_DC(predict=3,servo_door= servo_door )
        