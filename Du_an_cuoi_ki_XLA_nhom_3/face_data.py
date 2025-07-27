import cv2
import os

# Tạo thư mục lưu ảnh nếu chưa tồn tại
folder_name = "face_album"
os.makedirs(folder_name, exist_ok=True)

# Load bộ phát hiện khuôn mặt
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Mở camera
cap = cv2.VideoCapture(0)

print("Nhấn 's' để lưu ảnh khuôn mặt, 'x' để thoát.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Vẽ khung quanh mặt người
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        face_img = frame[y:y+h, x:x+w]

        cv2.imshow("Face", face_img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Hỏi người dùng nhập tên file
            img_name = input("Nhập tên ảnh (không cần phần mở rộng): ").strip()
            if img_name:
                img_path = os.path.join(folder_name, f"{img_name}.jpg")
                cv2.imwrite(img_path, face_img)
                print(f"Đã lưu ảnh vào: {img_path}")

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()
