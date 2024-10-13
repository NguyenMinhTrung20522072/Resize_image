import os
from tkinter import Tk, Label, Button, filedialog, messagebox, StringVar, Entry
from PIL import Image

# Hàm resize ảnh
def resize_image(image_path, output_path, target_size):
    with Image.open(image_path) as img:
        width, height = img.size
        if width < height:
            new_width = target_size
            new_height = int((new_width / width) * height)
        else:
            new_height = target_size
            new_width = int((new_height / height) * width)
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(output_path, format='PNG')
        return new_width, new_height

# Hàm duyệt thư mục ảnh và xử lý tất cả các ảnh
def resize_images_in_folders(input_folder, output_folder, target_size, progress_label, file_info_label, root):
    total_files = 0
    processed_files = 0
    for root_dir, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
                total_files += 1
    for root_dir, dirs, files in os.walk(input_folder):
        relative_path = os.path.relpath(root_dir, input_folder)
        output_dir = os.path.join(output_folder, relative_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
                input_path = os.path.join(root_dir, file)
                output_path = os.path.join(output_dir, f"{os.path.splitext(file)[0]}.png")
                new_width, new_height = resize_image(input_path, output_path, target_size)
                processed_files += 1
                # Cập nhật tiến trình
                progress_label.config(text=f"Đã xử lý {processed_files}/{total_files} ảnh")
                # Cập nhật thông tin ảnh đã xử lý
                file_info_label.config(text=f"Ảnh: {file} ({new_width}x{new_height})")
                progress_label.update()
                file_info_label.update()

    answer = messagebox.askquestion("Hoàn thành", "Tất cả các ảnh đã được thay đổi kích thước. Bạn có muốn tiếp tục resize không?")
    if answer == 'no':
        root.destroy()  # Đóng ứng dụng

# Hàm xử lý khi người dùng nhấn nút "Chọn thư mục nguồn"
def select_input_folder():
    folder_selected = filedialog.askdirectory()
    input_folder_path.set(folder_selected)

# Hàm xử lý khi người dùng nhấn nút "Chọn thư mục đích"
def select_output_folder():
    folder_selected = filedialog.askdirectory()
    output_folder_path.set(folder_selected)

# Hàm xử lý khi người dùng nhấn nút "Render"
def start_resizing():
    input_folder = input_folder_path.get()
    output_folder = output_folder_path.get()
    target_size = size_entry.get()
    if not input_folder or not output_folder:
        messagebox.showerror("Lỗi", "Vui lòng chọn cả thư mục nguồn và thư mục đích!")
        return
    try:
        target_size = int(target_size)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập một số cho kích thước tối thiểu!")
        return
    resize_images_in_folders(input_folder, output_folder, target_size, progress_label, file_info_label, root)

# Hàm xác nhận đóng ứng dụng
def on_closing():
    if messagebox.askokcancel("Xác nhận", "Bạn có chắc chắn muốn đóng ứng dụng không?"):
        root.destroy()

# Tạo cửa sổ chính
root = Tk()
root.title("Ứng dụng Resize Ảnh")
window_width = 400
window_height = 600

# Căn giữa màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Đặt sự kiện đóng cửa sổ
root.protocol("WM_DELETE_WINDOW", on_closing)

# Biến lưu đường dẫn thư mục
input_folder_path = StringVar()
output_folder_path = StringVar()

# Hàm xử lý khi người dùng nhấn nút "Chọn thư mục nguồn"
Label(root, text="", font=("Helvetica", 12)).pack(pady=20)
Label(root, text="Thư mục nguồn:", font=("Helvetica", 12)).pack(pady=5)
Button(root, text="Chọn thư mục nguồn", command=select_input_folder, font=("Helvetica", 12)).pack(pady=5)
Label(root, textvariable=input_folder_path, wraplength=400, font=("Helvetica", 10)).pack(pady=5)
Label(root, text="Thư mục đích:", font=("Helvetica", 12)).pack(pady=5)
Button(root, text="Chọn thư mục đích", command=select_output_folder, font=("Helvetica", 12)).pack(pady=5)
Label(root, textvariable=output_folder_path, wraplength=400, font=("Helvetica", 10)).pack(pady=5)
Label(root, text="Kích thước tối thiểu:", font=("Helvetica", 12)).pack(pady=5)
size_entry = Entry(root, font=("Helvetica", 12))
size_entry.pack(pady=5)
size_entry.insert(0, "2000")
progress_label = Label(root, text="Chưa bắt đầu", font=("Helvetica", 12))
progress_label.pack(pady=10)
file_info_label = Label(root, text="", font=("Helvetica", 12))
file_info_label.pack(pady=5)
Button(root, text="Render", command=start_resizing, font=("Helvetica", 12)).pack(pady=20)

root.mainloop()
