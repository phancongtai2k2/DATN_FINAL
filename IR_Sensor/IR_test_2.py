import RPi.GPIO as GPIO
import time

sensor = 16  # Chan GPIO23, chan vat 16

GPIO.setmode(GPIO.BOARD)  # Thiet lap che do danh so chan GPIO theo so do chan vat ly
GPIO.setup(sensor, GPIO.IN)  # Thiet lap chan GPIO23 (sensor) la dau vao (INPUT)

print("IR Sensor Ready.....")  # In thong bao cam bien da san sang hoat dong
print(" ")  # In ra mot dong trong

try: 
    while True:  # Vong lap vo han de lien tuc kiem tra trang thai cua cam bien
        print(GPIO.input(sensor))
        if GPIO.input(sensor)==1:  # Kiem tra trang thai cua chan cam bien
            print("Khong phat hien vat the")  # In ra gia tri 0 khi khong phat hien vat can
            
        else:  
            print("Phat hien vat the")  # In ra gia tri 1 khi co phat hien vat can
            time.sleep(1)  # Cho 200 ms truoc khi kiem tra lai

except KeyboardInterrupt:  # Bat ngoai le khi nguoi dung nhan Ctrl+C de dung chuong trinh
    GPIO.cleanup()  # Dat lai trang thai cua cac chan GPIO