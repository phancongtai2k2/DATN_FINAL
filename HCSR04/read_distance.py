import RPi.GPIO as GPIO  # Thu vien dieu khien GPIO cua Raspberry Pi
import time  # Thu vien xu ly thoi gian

def measure_distance():
    # Cau hinh GPIO
    GPIO.setwarnings(False)  # Tat canh bao
    GPIO.setmode(GPIO.BCM)  # Dat che do danh so GPIO theo chuan BCM

    TRIG = 23  # Dat chan GPIO 23 cho TRIG
    ECHO = 24  # Dat chan GPIO 24 cho ECHO

    print("Distance Measurement In Progress")  # In thong bao bat dau do khoang cach

    GPIO.setup(TRIG, GPIO.OUT)  # Dat chan TRIG lam dau ra
    GPIO.setup(ECHO, GPIO.IN)  # Dat chan ECHO lam dau vao

    try:
        while True:  # Vong lap vo han de do lien tuc
            GPIO.output(TRIG, False)  # Dam bao chan TRIG dang o muc thap
            print("Waiting For Sensor To Settle")  # In thong bao cho cam bien on dinh
            time.sleep(2)  # Cho 2 giay cho cam bien on dinh

            GPIO.output(TRIG, True)  # Dat chan TRIG len muc cao
            time.sleep(0.00001)  # Giu chan TRIG o muc cao trong 10 micro giay
            GPIO.output(TRIG, False)  # Dat chan TRIG tro lai muc thap

            while GPIO.input(ECHO) == 0:  # Cho ECHO len muc cao
                pulse_start = time.time()  # Ghi lai thoi diem bat dau xung

            while GPIO.input(ECHO) == 1:  # Cho ECHO xuong muc thap
                pulse_end = time.time()  # Ghi lai thoi diem ket thuc xung

            pulse_duration = pulse_end - pulse_start  # Tinh toan do dai xung

            distance = pulse_duration * 17150  # Tinh toan khoang cach dua tren do dai xung
            distance = round(distance, 2)  # Lam tron khoang cach den 2 chu so thap phan

            print("Distance:", distance, "cm")  # In khoang cach do duoc

            if distance < 10:  # Kiem tra neu khoang cach duoi 10 cm
                print("Distance is below 10 cm, stopping measurement")  # In thong bao va thoat khoi vong lap
                break
            
            time.sleep(1)  # Cho 1 giay truoc khi do lai

    except KeyboardInterrupt:  # Xu ly khi nguoi dung nhan Ctrl+C de dung chuong trinh
        print("Measurement stopped by User")  # In thong bao dung do
    finally:
        GPIO.cleanup()  # Don dep cac chan GPIO

def another_function():
    print("Executing another function")  # Thay the bang code thuc te cua ban

# Goi ham do khoang cach
# measure_distance()