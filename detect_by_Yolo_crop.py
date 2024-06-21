from ultralytics import YOLO
import cv2
from time import sleep
import os

# Tai mo hinh YOLO tu file 'models/last.pt'
model = YOLO("models/last.pt")

# Mo ket noi voi webcam (thiet bi webcam co chi so la 0)
webcam = cv2.VideoCapture(0)

def detect_yolov8():
    class_number = 4
    class_name = ""
    while True:
        try:
            # Doc khung hinh tu webcam
            check, frame = webcam.read()

            # Hien thi khung hinh trong cua so co ten "Capturing"
            cv2.imshow("Capturing", frame)

            # Luu khung hinh da chup thanh file 'saved_img.jpg' trong thu muc 'save_image'
            path = "save_image"
            if not os.path.exists(path):
                os.makedirs(path)
            img_path = os.path.join(path, 'saved_img.jpg')
            cv2.imwrite(img_path, frame)
            
            # Thoat vong lap
            break

        except KeyboardInterrupt:
            # Neu co loi KeyboardInterrupt (nhan Ctrl+C), thi dung webcam va thoat
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    # Ap dung cat anh de chi bao gom vung chua cai chai trong ong
    img = cv2.imread(img_path)  # Doc hinh anh tu file 'saved_img.jpg'
    
    # Xac dinh toa do vung chua cai chai trong ong
    x, y, w, h = 190, 100, 230, 400  # Cac gia tri nay la vi du, can dieu chinh theo thuc te
    
    # Cat vung chua cai chai
    cropped_img = img[y:y+h, x:x+w]
    
    # Luu hinh anh da cat
    cropped_img_path = os.path.join(path, 'cropped_saved_img.jpg')
    cv2.imwrite(cropped_img_path, cropped_img)

    # Thuc hien phat hien doi tuong tren hinh anh da cat
    print("Chuan bi detect tren anh da cat")
    results = model.predict(source=cropped_img_path, save=True, show=True)  # Su dung mo hinh YOLO de du doan doi tuong tren hinh anh da cat
    sleep(1)
    print("Ket thuc detect")

    for r in results:
        for c in r.boxes.cls:
            class_number = int(c)  # Lay so lop (class number) cua doi tuong duoc phat hien
            class_name = model.names[int(c)]  # Lay ten lop (class name) cua doi tuong duoc phat hien

    print("Gia tri tra ve: ", class_name, " voi id:", class_number)

    # # Luu lai anh da duoc YOLO ve khung chu
    # for result in results:
    #     # Lay hinh anh da duoc YOLO ve khung
    #     annotated_frame = result.plot()  # Ham nay tra ve hinh anh da ve khung

    #     # Luu hinh anh da ve khung
    #     detected_img_path = os.path.join(path, 'detected_cropped_img.jpg')
    #     cv2.imwrite(detected_img_path, annotated_frame)
    #     print(f"Anh da detect duoc luu tai: {detected_img_path}")



    # Luu lai anh da duoc YOLO ve khung chu (bo qua phan tram do chac chan)
    for result in results:
        annotated_frame = cropped_img.copy()  # Tao ban sao cua anh da cat
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Lay toa do khung chu (bounding box)
            label = model.names[int(box.cls[0])]  # Lay ten lop
            # Ve khung chu
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Ve ten lop len anh
            cv2.putText(annotated_frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Luu hinh anh da ve khung chu
        detected_img_path = os.path.join(path, 'detected_cropped_img.jpg')
        cv2.imwrite(detected_img_path, annotated_frame)
        print(f"Anh da detect duoc luu tai: {detected_img_path}")



    
    cv2.destroyAllWindows()  # Dong tat ca cac cua so OpenCV
    return class_number
