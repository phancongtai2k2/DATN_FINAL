from ultralytics import YOLO
import cv2
from time import sleep
import os
from PIL import Image
model = YOLO("models\last.pt")
webcam = cv2.VideoCapture(0)

def detect_yolov8():
    class_number=4
    class_name=""
    while True:
        try:
            # Đọc khung hình từ webcam
            check, frame = webcam.read()

            # Hiển thị khung hình trong cửa sổ
            cv2.imshow("Capturing", frame)
        
            # Lưu ảnh đã chụp
            path = "save_image"
            cv2.imwrite(os.path.join(path,'saved_img.jpg'), frame)
            
            # Thoát vòng lặp
            break

        except KeyboardInterrupt:
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    # Thực hiện phát hiện đối tượng trên ảnh đã chụp
    print("Chuan bi detect")
    im1 = "save_image/saved_img.jpg"
    results = model.predict(source=im1, show=True)  # lưu hình ảnh
    print("Ket thuc detect")

    for r in results:
        for c in r.boxes.cls:
            class_number=int(c)
            class_name=model.names[int(c)]

    print("Gia tri tra ve: ",class_name, " voi id:",class_number)
    
    cv2.destroyAllWindows()