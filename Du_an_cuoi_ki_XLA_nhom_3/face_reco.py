import cv2
import face_recognition
import os
import numpy as np

#Đường dẫn đến thư mục chứa album ảnh khuôn mặt
ALBUM_PATH = "face_album"  

#Tạo danh sách các khuôn mặt đã biết và tên tương ứng
known_face_encodings = []
known_face_names = []

#Đọc các ảnh từ album và tạo encodings
for filename in os.listdir(ALBUM_PATH):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(ALBUM_PATH, filename)
        try:
            known_image = face_recognition.load_image_file(image_path)
            face_encodings_in_image = face_recognition.face_encodings(known_image)
            if len(face_encodings_in_image) > 0:
                known_face_encodings.append(face_encodings_in_image[0])
                known_face_names.append(os.path.splitext(filename)[0])
            else:
                print(f"Không tìm thấy khuôn mặt nào trong ảnh: {filename}")
        except Exception as e:
            print(f"Lỗi khi tải ảnh {filename}: {e}")

#Khởi tạo camera
video_capture = cv2.VideoCapture(0)

#Hướng dẫn
print("Nhấn 'x' để thoát.")

while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Không thể truy cập camera.")
        break

    #Tìm tất cả các khuôn mặt trong frame hiện tại
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    #Lặp qua từng khuôn mặt được tìm thấy trong frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #So sánh khuôn mặt trong frame với các khuôn mặt đã biết
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Không xác định"
        #Nếu tìm thấy khuôn mặt khớp
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
        #Vẽ khung và tên lên khuôn mặt
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)

    #Hiển thị kết quả lên màn hình
    cv2.imshow('Nhận diện khuôn mặt', frame)
    #Cài đặt phím phím 'x'
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
#Mở camera
video_capture.release()
cv2.destroyAllWindows()