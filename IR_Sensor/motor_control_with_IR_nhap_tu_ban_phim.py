import RPi.GPIO as GPIO
import time

def motor_control_with_ir():
    # Thiết lập chân GPIO cho động cơ và cảm biến hồng ngoại
    motorPin1 = 27  # Chân GPIO 27, chân vật lý 13
    motorPin2 = 26  # Chân GPIO 26, chân vật lý 37
    enablePin = 14  # Chân GPIO 14, chân vật lý 8 (UART TXD)
    irSensorPin1 = 4  # Chân GPIO 4, chân vật lý 7
    irSensorPin2 = 16 # Chân GPIO 16, chân vật lý 36
    irSensorPin3 = 17 # Chân GPIO 17, chân vật lý 11
    irSensorPin4 = 21 # Chân GPIO 21, chân vật lý 40

    keepRunning = True  # Biến cờ để kiểm soát việc tiếp tục hoặc dừng vòng lặp

    # Thiết lập GPIO
    GPIO.setmode(GPIO.BCM)  # Thiết lập chế độ đánh số chân GPIO theo chuẩn BCM
    GPIO.setup(motorPin1, GPIO.OUT)  # Thiết lập chân motorPin1 là OUTPUT
    GPIO.setup(motorPin2, GPIO.OUT)  # Thiết lập chân motorPin2 là OUTPUT
    GPIO.setup(enablePin, GPIO.OUT)  # Thiết lập chân enablePin là OUTPUT
    GPIO.setup(irSensorPin1, GPIO.IN)  # Thiết lập chân irSensorPin1 là INPUT
    GPIO.setup(irSensorPin2, GPIO.IN)  # Thiết lập chân irSensorPin2 là INPUT
    GPIO.setup(irSensorPin3, GPIO.IN)  # Thiết lập chân irSensorPin3 là INPUT
    GPIO.setup(irSensorPin4, GPIO.IN)  # Thiết lập chân irSensorPin4 là INPUT

    # Khởi tạo PWM cho chân enablePin
    pwm = GPIO.PWM(enablePin, 1000)  # Thiết lập PWM với tần số 1000 Hz
    pwm.start(0)  # Bắt đầu PWM với độ rộng xung 0%

    print("Raspberry Pi DC Motor Control with IR Sensor - Start")  # In thông báo khởi động

    def rotate_motor(clockwise, speed):
        if clockwise:
            GPIO.output(motorPin1, GPIO.HIGH)  # Thiết lập motorPin1 là HIGH
            GPIO.output(motorPin2, GPIO.LOW)  # Thiết lập motorPin2 là LOW
        else:
            GPIO.output(motorPin1, GPIO.LOW)  # Thiết lập motorPin1 là LOW
            GPIO.output(motorPin2, GPIO.HIGH)  # Thiết lập motorPin2 là HIGH
        pwm.ChangeDutyCycle(speed)  # Thay đổi độ rộng xung PWM

    try:
        while keepRunning:
            data = input("Please enter the value of i: ")  # Nhập dữ liệu từ terminal
            if data.isdigit():
                i = int(data)  # Chuyển đổi dữ liệu thành số nguyên
                print(f"Value of i entered: {i}")
                irValueSetup = None

                if i == 1:
                    irValueSetup = irSensorPin1  # Chọn cảm biến hồng ngoại 1
                    print("Stop 1")
                elif i == 2:
                    irValueSetup = irSensorPin2  # Chọn cảm biến hồng ngoại 2
                    print("Stop 2")
                elif i == 3:
                    irValueSetup = irSensorPin3  # Chọn cảm biến hồng ngoại 3
                    print("Stop 3")
                elif i == 4:
                    irValueSetup = irSensorPin4  # Chọn cảm biến hồng ngoại 4
                    print("Stop 4")
                else:
                    print("Nhập lại i")  # Thông báo nhập lại giá trị i nếu không hợp lệ
                    continue

                while keepRunning:
                    irValue = GPIO.input(irSensorPin1)  # Đọc giá trị từ cảm biến hồng ngoại 1
                    print(irValue)

                    rotate_motor(clockwise=True, speed=70)  # Điều khiển động cơ quay theo chiều kim đồng hồ với tốc độ 70%
                    time.sleep(0.1)  # Chờ 100 ms

                    if GPIO.input(irValueSetup) != GPIO.HIGH:
                        print("Object detected.........., stopping motor")
                        rotate_motor(clockwise=True, speed=0)  # Dừng động cơ
                        time.sleep(4)  # Chờ 4000 ms để đảm bảo động cơ dừng

                    if irValue != GPIO.HIGH:
                        print("Object detected, stopping motor")
                        rotate_motor(clockwise=True, speed=0)  # Dừng động cơ
                        time.sleep(10)  # Chờ 10000 ms để đảm bảo động cơ dừng
                        keepRunning = False  # Đặt cờ để dừng vòng lặp
                        break  # Thoát khỏi vòng lặp hiện tại
    except KeyboardInterrupt:
        print("Program interrupted")
    finally:
        GPIO.cleanup()  # Đặt lại trạng thái của các chân GPIO

# Gọi hàm điều khiển động cơ
motor_control_with_ir()