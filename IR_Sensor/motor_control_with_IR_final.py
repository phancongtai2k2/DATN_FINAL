import RPi.GPIO as GPIO
import time

def motor_control_with_ir(i):
    # Thiet lap chan GPIO cho dong co va cam bien hong ngoai
    motorPin1 = 27  # Chan GPIO 27, chan vat ly 13
    motorPin2 = 26  # Chan GPIO 26, chan vat ly 37
    enablePin = 14  # Chan GPIO 14, chan vat ly 8 (UART TXD)
    irSensorPin1 = 4  # Chan GPIO 4, chan vat ly 7
    irSensorPin2 = 16 # Chan GPIO 16, chan vat ly 36
    irSensorPin3 = 17 # Chan GPIO 17, chan vat ly 11
    irSensorPin4 = 21 # Chan GPIO 21, chan vat ly 40

    keepRunning = True  # Bien co de kiem soat viec tiep tuc hoac dung vong lap

    # Thiet lap GPIO
    GPIO.setmode(GPIO.BCM)  # Thiet lap che do danh so chan GPIO theo chuan BCM
    GPIO.setup(motorPin1, GPIO.OUT)  # Thiet lap chan motorPin1 la OUTPUT
    GPIO.setup(motorPin2, GPIO.OUT)  # Thiet lap chan motorPin2 la OUTPUT
    GPIO.setup(enablePin, GPIO.OUT)  # Thiet lap chan enablePin la OUTPUT
    GPIO.setup(irSensorPin1, GPIO.IN)  # Thiet lap chan irSensorPin1 la INPUT
    GPIO.setup(irSensorPin2, GPIO.IN)  # Thiet lap chan irSensorPin2 la INPUT
    GPIO.setup(irSensorPin3, GPIO.IN)  # Thiet lap chan irSensorPin3 la INPUT
    GPIO.setup(irSensorPin4, GPIO.IN)  # Thiet lap chan irSensorPin4 la INPUT

    # Khoi tao PWM cho chan enablePin
    pwm = GPIO.PWM(enablePin, 1000)  # Thiet lap PWM voi tan so 1000 Hz
    pwm.start(0)  # Bat dau PWM voi do rong xung 0%

    print("Raspberry Pi DC Motor Control with IR Sensor - Start")  # In thong bao khoi dong

    def rotate_motor(clockwise, speed):
        if clockwise:
            GPIO.output(motorPin1, GPIO.HIGH)  # Thiet lap motorPin1 la HIGH
            GPIO.output(motorPin2, GPIO.LOW)  # Thiet lap motorPin2 la LOW
        else:
            GPIO.output(motorPin1, GPIO.LOW)  # Thiet lap motorPin1 la LOW
            GPIO.output(motorPin2, GPIO.HIGH)  # Thiet lap motorPin2 la HIGH
        pwm.ChangeDutyCycle(speed)  # Thay doi do rong xung PWM

    try:
        print(f"Value of i entered: {i}")
        irValueSetup = None

        if i == 1:
            irValueSetup = irSensorPin1  # Chon cam bien hong ngoai 1
            print("Stop 1")
        elif i == 2:
            irValueSetup = irSensorPin2  # Chon cam bien hong ngoai 2
            print("Stop 2")
        elif i == 3:
            irValueSetup = irSensorPin3  # Chon cam bien hong ngoai 3
            print("Stop 3")
        elif i == 4:
            irValueSetup = irSensorPin4  # Chon cam bien hong ngoai 4
            print("Stop 4")
        else:
            print("Nhap lai i")  # Thong bao nhap lai gia tri i neu khong hop le
            return

        while keepRunning:
            irValue = GPIO.input(irSensorPin1)  # Doc gia tri tu cam bien hong ngoai 1
            print(irValue)

            rotate_motor(clockwise=True, speed=70)  # Dieu khien dong co quay theo chieu kim dong ho voi toc do 70%
            time.sleep(0.1)  # Cho 100 ms

            if GPIO.input(irValueSetup) != GPIO.HIGH:
                print("Object detected.........., stopping motor")
                rotate_motor(clockwise=True, speed=0)  # Dung dong co
                time.sleep(4)  # Cho 4000 ms de dam bao dong co dung

            if irValue != GPIO.HIGH:
                print("Object detected, stopping motor")
                rotate_motor(clockwise=True, speed=0)  # Dung dong co
                time.sleep(10)  # Cho 10000 ms de dam bao dong co dung
                keepRunning = False  # Dat co de dung vong lap
                break  # Thoat khoi vong lap hien tai
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()  # Dat lai trang thai cua cac chan GPIO

# Goi ham dieu khien dong co voi tham so dau vao
motor_control_with_ir(3)  # Thay gia tri 1 bang gia tri ban muon kiem tra
