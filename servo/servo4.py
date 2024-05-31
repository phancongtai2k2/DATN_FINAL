from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

# Tao mot factory cho PiGPIO, cho phep giao tiep voi cac chan GPIO cua Raspberry Pi qua pigpio daemon
factory = PiGPIOFactory()

# Tao mot doi tuong Servo ket noi voi chan GPIO so 17
# Tham so min_pulse_width va max_pulse_width xac dinh do rong xung toi thieu va toi da de dieu khien servo
servo = Servo(17, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

print("Start in the middle")
# Di chuyen servo den vi tri giua (0 do)
servo.mid()
sleep(5)  # Dung lai 5 giay

print("Go to min")
# Di chuyen servo den vi tri toi thieu (thuong la -90 do)
servo.min()
sleep(5)  # Dung lai 5 giay

print("Go to max")
# Di chuyen servo den vi tri toi da (thuong la +90 do)
servo.max()
sleep(5)  # Dung lai 5 giay

print("And back to middle")
# Di chuyen servo tro lai vi tri giua (0 do)
servo.mid()
sleep(5)  # Dung lai 5 giay

# Dung servo, tra lai gia tri None de ngung gui tin hieu den servo
servo.value = None
