# Nhập Môn Xử Lý Ảnh Số - Đồ Án Cuối Kì  
## **Face Reconigtion**
- **Nhóm thực hiện:** Nhóm 3
- **Sinh viên thực hiện:** Hà Đại Vĩ - Đoàn Nhật Khôi - Phạm Thanh Tùng - Lê Hữu Khang
- **Giảng viên:** Đỗ Hữu Quân  

---

## Tổng quan dự án

Trong thời đại công nghệ số, nhận diện khuôn mặt ngày càng trở nên phổ biến và ứng dụng rộng rãi trong các lĩnh vực như an ninh, điểm danh tự động, quản lý ra vào, và tương tác thông minh với thiết bị. Đề tài "Xây dựng hệ thống nhận diện khuôn mặt thời gian thực sử dụng Python và OpenCV" được chọn nhằm mục tiêu tìm hiểu sâu hơn về các kỹ thuật xử lý ảnh, trích xuất đặc trưng khuôn mặt, và ứng dụng chúng trong thực tiễn với công nghệ đơn giản, dễ triển khai.

---

## Tính năng chính 

- **Thu thập dữ liệu khuôn mặt:** Giao diện camera cho phép người dùng chụp và lưu ảnh khuôn mặt kèm tên tương ứng.
- **Trích xuất đặc trưng:** Sử dụng face_recognition để mã hóa khuôn mặt thành vector đặc trưng.
- **Phát hiện khuôn mặt thời gian thực:** Sử dụng Haar Cascade để phát hiện khuôn mặt trong khung hình video.
- **Nhận diện khuôn mặt:** So sánh vector đặc trưng với dữ liệu đã thu thập để xác định danh tính người trong thời gian thực.
- **Hiển thị real-time:** Hệ thống hiển thị Bounding Box và tên người ngay trên webcam, trực quan và chính xác.
- **Quản lý dữ liệu đơn giản:** Dữ liệu khuôn mặt được lưu cục bộ theo dạng file ảnh, dễ chỉnh sửa và mở rộng.
  
---

## Công nghệ sử dụng

- **OpenCV:** Thư viện xử lý ảnh và video mạnh mẽ, dùng để truy xuất webcam và phát hiện khuôn mặt.
- **face_recognition:** Thư viện nhận diện khuôn mặt dựa trên Deep Learning, đơn giản nhưng hiệu quả.
- **Haar Cascade Classifier:** Mô hình học máy truyền thống dùng để phát hiện khuôn mặt trong ảnh.
- **NumPy:** Thư viện xử lý mảng, dùng để hỗ trợ thao tác dữ liệu ảnh và vector đặc trưng.
- **Python:** Ngôn ngữ chính cho toàn bộ hệ thống, đơn giản, linh hoạt và dễ triển khai.
---

## HƯỚNG DẪN CÀI ĐẶT VÀ SỬ DỤNG HỆ THỐNG THU THẬP VÀ NHẬN DIỆN KHUÔN MẶT
**Các yêu cầu chuẩn bị**

**Python**
```
Phiên bản khuyến nghị: Python 3.6 – 3.10
```

**Thư viện Python**
Cài đặt bằng pip:
```
pip install numpy opencv-python scikit-learn
```

**File cascade phát hiện khuôn mặt**

- File haarcascade_frontalface_alt.xml phải có trong thư mục code.
- Hoặc dùng đường dẫn mặc định của OpenCV:
```
cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml")
```

**Tạo thư mục lưu dữ liệu khuôn mặt**
Trong thư mục dự án, tạo thư mục:
```
./face_dataset/
```
Thư mục này sẽ chứa các file .npy lưu dữ liệu khuôn mặt.

---

## **Các bước chạy chương trình thu thập dữ liệu khuôn mặt**
Đây là đoạn code thứ nhất, để thu thập dữ liệu và lưu thành file .npy.

- **1.** Chạy script Python:
```
python face_data.py
```

- **2.** Nhập tên người cần thu thập dữ liệu, ví dụ:
```
Enter the name of person : Vi
```

- **3.** Hệ thống sẽ bật webcam và phát hiện khuôn mặt.
```
Mỗi khi webcam bắt được khuôn mặt, sẽ vẽ khung xanh.
Sau mỗi 10 khung hình, tự động lưu thêm một ảnh vào tập dữ liệu.
```

- **4.** Kết thúc thu thập dữ liệu:
Nhấn phím q để dừng chương trình.
Chương trình sẽ lưu dữ liệu dưới dạng:
```
./face_dataset/Vi.npy
```

- **5.** Kết quả
File .npy chứa mảng dữ liệu ảnh khuôn mặt đã thu thập.

## **Các bước chạy chương trình nhận diện khuôn mặt**
Đây là đoạn code thứ hai, dùng để nhận diện khuôn mặt thời gian thực.
- **1.** Đảm bảo thư mục face_dataset có ít nhất một file .npy đã được thu thập từ bước trước.

- **2️.** Chạy script Python:
```
python face_recognition.py
```
- **3.** Hệ thống sẽ tải toàn bộ dữ liệu khuôn mặt, huấn luyện mô hình nhận diện.
Thông tin hiển thị:
```[INFO] Loaded training data:
  Faces: (số lượng ảnh, kích thước vector)
  Labels: (số lượng nhãn)
```
- **4.** Mở webcam nhận diện khuôn mặt.
Nếu phát hiện khuôn mặt:
```
Sẽ vẽ khung chữ nhật (xanh lá: nhận diện được, đỏ: Unknown).
Hiển thị tên người trên hình.
```

- **5️.** Kết thúc nhận diện:
```
Nhấn phím q để dừng chương trình.
```

---

**Một số lưu ý**
Nếu không nhận diện được khuôn mặt:
```
Kiểm tra ánh sáng webcam.
Đảm bảo khoảng cách mặt – camera không quá xa.
Nếu hiện "Unknown":
Mô hình nhận diện khoảng cách quá lớn so với dữ liệu huấn luyện.
Cần thu thập thêm dữ liệu hoặc giảm THRESHOLD trong mã nhận diện.
Cập nhật dữ liệu nhận diện mới:
Chạy lại chương trình thu thập dữ liệu với tên mới.
Sau đó chạy lại chương trình nhận diện.
```

**Tóm tắt quy trình sử dụng**
Thu thập dữ liệu khuôn mặt:
```
Chạy script thứ nhất.
Nhập tên.
Nhấn q để lưu.
```

Huấn luyện và nhận diện:
```
Chạy script thứ hai.
Hệ thống tự động huấn luyện.
Nhận diện thời gian thực.
```

---

## Tài liệu tham khảo

- [Digital Image Processing - Rafael C. Gonzalez](https://www.amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/013168728X)
- [OpenCV Documentation](https://docs.opencv.org/)
- Slide bài giảng Nhập môn Xử lý ảnh số - Văn Lang University
