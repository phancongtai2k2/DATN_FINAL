import RPi.GPIO as GPIO
import time

class IRSensor:
    def __init__(self, pin):
        self.sensor = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor, GPIO.IN)
        print("IR Sensor Ready.....")
        print(" ")

    def read_sensor(self):
        t = 0
        try: 
            while True:
                if GPIO.input(self.sensor):
                    print("No Object Detected: 0")
                    time.sleep(0.2)
                else:  
                    print("Object Detected: 1")
                    t = 1
                    break

        except KeyboardInterrupt:
            GPIO.cleanup()
        return t

# # Sử dụng class IRSensor
# ir_sensor = IRSensor(pin=23)
# t = ir_sensor.read_sensor()
