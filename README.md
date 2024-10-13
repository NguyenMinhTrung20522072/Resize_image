# Ứng Dụng Resize Ảnh

## Giới Thiệu

Ứng dụng này cho phép người dùng thay đổi kích thước của nhiều ảnh cùng lúc. Bạn có thể chọn thư mục chứa ảnh và thư mục đích để lưu ảnh đã được resize. Ứng dụng hỗ trợ định dạng ảnh phổ biến như JPG, JPEG, PNG, BMP và TIFF.

## Tính Năng

- Chọn thư mục chứa ảnh để thay đổi kích thước.
- Chọn thư mục lưu ảnh đã được thay đổi kích thước.
- Nhập kích thước tối thiểu cho chiều dài hoặc chiều cao của ảnh.
- Hiển thị tiến trình xử lý ảnh và thông tin của ảnh hiện tại.
- Xác nhận khi hoàn thành việc resize và lựa chọn tiếp tục hoặc đóng ứng dụng.
- Xác nhận khi người dùng muốn đóng ứng dụng.

## Cài Đặt

### Yêu Cầu

- Python 3.x
- Thư viện `Pillow` cho xử lý ảnh.
- Thư viện `tkinter` cho giao diện người dùng.

### Cài Đặt Pillow

Bạn có thể cài đặt Pillow bằng lệnh sau:

```bash
pip install Pillow
```



## Sử Dụng
1. Mở ứng dụng app_resize.exe.
2. Nhấp vào nút "Chọn thư mục nguồn" để chọn thư mục chứa ảnh cần resize.
3. Nhấp vào nút "Chọn thư mục đích" để chọn nơi lưu ảnh đã được resize.
4. Nhập kích thước tối thiểu mà bạn muốn cho ảnh.
5. Nhấp vào nút "Render" để bắt đầu quá trình resize.
6. Xem tiến trình và thông tin ảnh đã xử lý.
7. Khi hoàn thành, bạn có thể chọn tiếp tục resize hoặc đóng ứng dụng.
## Ghi Chú
- Ứng dụng sẽ hiển thị một cửa sổ xác nhận khi bạn cố gắng đóng ứng dụng.
- Tất cả các ảnh sẽ được lưu dưới định dạng PNG trong thư mục đích.
- Bạn có thể tải file resize.exe để có thể sử dụng trực tiếp mà không cần cài đặt môi trường Python.
