import RPi.GPIO as GPIO
import time

class MotorControl(object):

    def __init__(self, in1, in2, ena):
        # Thiet lap cac chan GPIO
        self.IN1 = in1  # Chan GPIO dieu khien IN1
        self.IN2 = in2  # Chan GPIO dieu khien IN2
        self.ENA = ena  # Chan GPIO dieu khien ENA (PWM)

        GPIO.setmode(GPIO.BCM)  # Thiet lap che do danh so chan GPIO theo chuan BCM
        # GPIO.setwarnings(False)  # Tat canh bao ve GPIO

        # Thiet lap cac chan GPIO la OUTPUT
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.ENA, GPIO.OUT)

        self.stop()  # Dung dong co ban dau
        self.PWM = GPIO.PWM(self.ENA, 500)  # Thiet lap PWM voi tan so 500 Hz
        self.PWM.start(50)  # Bat dau PWM voi do rong xung 50%

    def forward(self):
        # Dieu khien dong co quay thuan
        GPIO.output(self.IN1, GPIO.HIGH)
        GPIO.output(self.IN2, GPIO.LOW)

    def backward(self):
        # Dieu khien dong co quay nguoc
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.HIGH)

    def stop(self):
        # Dung dong co
        GPIO.output(self.IN1, GPIO.LOW)
        GPIO.output(self.IN2, GPIO.LOW)

    def setSpeed(self, value):
        # Dieu chinh toc do dong co
        self.PWM.ChangeDutyCycle(value)

# try:
#     motor = MotorControl(in1=27, in2=22, ena=14)  # Khoi tao doi tuong dieu khien dong co

#     while True:
#         motor.forward()  # Quay thuan dong co
#         motor.setSpeed(75)  # Dieu chinh toc do dong co la 75%
#         time.sleep(2)  # Chay trong 2 giay

#         motor.backward()  # Quay nguoc dong co
#         motor.setSpeed(50)  # Dieu chinh toc do dong co la 50%
#         time.sleep(2)  # Chay trong 2 giay

#         motor.stop()  # Dung dong co
#         time.sleep(2)  # Dung trong 2 giay

# except KeyboardInterrupt:
#     # Bat ngoai le khi nhan Ctrl+C de dung chuong trinh
#     motor.stop()  # Dung dong co
#     GPIO.cleanup()  # Dat lai trang thai cua cac chan GPIO