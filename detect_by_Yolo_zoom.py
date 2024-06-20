from ultralytics import YOLO
import cv2
from time import sleep
import os
from PIL import Image

# Tai model YOLO
model = YOLO("models/last.pt")
# Mo ket noi den webcam
webcam = cv2.VideoCapture(0)

def detect_yolov8_zoom():
    class_number = 4
    class_name = ""
    
    while True:
        try:
            # Doc khung hinh tu webcam
            check, frame = webcam.read()

            # Hien thi khung hinh trong cua so
            cv2.imshow("Capturing", frame)
        
            # Tao thu muc luu anh neu chua co
            path = "save_image"
            os.makedirs(path, exist_ok=True)
            
            # Luu khung hinh da chup thanh anh
            image_path = os.path.join(path, 'saved_img.jpg')
            cv2.imwrite(image_path, frame)
            
            # Thoat vong lap
            break

        except KeyboardInterrupt:
            # Xu ly khi nhan phim Ctrl+C de ngat chuong trinh
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    # Phong to anh da chup len 2 lan
    img = cv2.imread(image_path)  # Doc anh tu file
    # Su dung cv2.resize de phong to anh
    zoomed_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Luu anh da phong to vao thu muc
    zoomed_image_path = os.path.join(path, 'saved_img_zoomed.jpg')
    cv2.imwrite(zoomed_image_path, zoomed_img)

    # Hien thi anh da phong to
    # cv2.imshow("Zoomed Image", zoomed_img)
    # sleep(1)
    
    # Thuc hien phat hien doi tuong tren anh da phong to
    print("Chuan bi detect")
    im1 = "save_image/saved_img_zoomed.jpg"
    results = model.predict(source=im1, show=True)  # Su dung anh phong to de phat hien doi tuong
    sleep(1)
    print("Ket thuc detect")

    # Lay thong tin ket qua tu model YOLO
    for r in results:
        for c in r.boxes.cls:
            class_number = int(c)
            class_name = model.names[int(c)]

    # In ra thong tin lop doi tuong va ID
    print("Gia tri tra ve: ", class_name, " voi id:", class_number)
    
    # Dong cua so hien thi
    cv2.destroyAllWindows()
    return class_number


