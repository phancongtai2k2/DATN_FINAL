# Lay thu vien chinh GPIO
import RPi.GPIO as GPIO
# Lay thu vien time
import time



# Ham cau hinh mot chan GPIO duy nhat
def setup_pin(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)  # Dat trang thai khoi tao la LOW

# Ham bat chan GPIO
def turn_on(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)  # Dat trang thai khoi tao la LOW
    GPIO.output(pin, GPIO.HIGH)  # Dat chan GPIO thanh HIGH (bat)
    print("Pin " + str(pin) + " is turned on")

# Ham tat chan GPIO
def turn_off(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)  # Dat trang thai khoi tao la LOW
    GPIO.output(pin, GPIO.LOW)  # Dat chan GPIO thanh LOW (tat)
    print("Pin " + str(pin) + " is turned off")

