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


## Tài liệu tham khảo

- [Digital Image Processing - Rafael C. Gonzalez](https://www.amazon.com/Digital-Image-Processing-Rafael-Gonzalez/dp/013168728X)
- [OpenCV Documentation](https://docs.opencv.org/)
- Slide bài giảng Nhập môn Xử lý ảnh số - Văn Lang University
