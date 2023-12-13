import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk  
import pandas as pd
import numpy as np


def open_csv():
    file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
    if file_path:

        df = pd.read_csv(file_path, encoding='cp1252')
        update_treeview(df)


def update_treeview(data):
    for item in tree.get_children():
        tree.delete(item)

    for index, row in data.iterrows():
        tree.insert("", "end", values=row.tolist())

    result_entry.delete(0, tk.END)
    result_entry.insert(0, ', '.join(map(str, data.iloc[0].tolist())))

def open_image():
    file_path = filedialog.askopenfilename(title="Open Image File", filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:

        img = Image.open(file_path)
        img = img.resize((220, 220), resample=Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(img)
        image_label.config(image=new_image)
        image_label.image = new_image

def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert height to meters
        bmi = weight / (height ** 2)
        result_entry.delete(0, tk.END)

        if bmi < 18.5:
            result_entry.insert(0, f'ผอม')
        elif 18.5 <= bmi < 24.9:
            result_entry.insert(0, f'สมส่วน')
        else:
            result_entry.insert(0, f'อ้วน')

    except ValueError:
        result_entry.delete(0, tk.END)
        result_entry.insert(0, 'กรุณาป้อนข้อมูลให้ถูกต้อง')

# ข้อมูลจาก NumPy array
data = np.array([
    [1, 27, 60, 170],
    [1, 18, 70, 180],
    [0, 19, 64, 174],
    [0, 25, 80, 167],
    [1, 40, 56, 172],
    [0, 32, 45, 156],
    [1, 24, 52, 170],
    [1, 28, 70, 180],
    [0, 19, 45, 165],
    [1, 20, 120, 165]
])

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("My GUI")

# สร้าง Treeview สำหรับแสดงตาราง
tree = ttk.Treeview(root, columns=(1, 2, 3, 4), show="headings", height=10)

image_label = tk.Label(root)
image_label.grid(row=0, column=2, padx=10, pady=10)

# กำหนดขนาดของคอลัมน์
tree.column(1, width=80)
tree.column(2, width=80)
tree.column(3, width=80)
tree.column(4, width=80)

# กำหนดชื่อคอลัมน์
tree.heading(1, text="เพศ")
tree.heading(2, text="อายุ")
tree.heading(3, text="น้ำหนัก")
tree.heading(4, text="ส่วนสูง")

# เพิ่มข้อมูลลงใน Treeview
for row in data:
    str_row = [str(element) for element in row]
    tree.insert("", "end", values=str_row)

# แสดง Treeview
tree.grid(row=0, column=1, padx=10, pady=10)

# สร้างปุ่มกด (เปิดไฟล์ CSV)
open_csv_button = tk.Button(root, text="Open CSV", command=open_csv)
open_csv_button.place(x=10, y=250)

# สร้างปุ่มกด (เปิดไฟล์รูปภาพ)
open_image_button = tk.Button(root, text="Open Image", command=open_image)
open_image_button.place(x=10, y=290)

# สร้างช่องใส่ข้อมูล 4 ช่อง พร้อมข้อความกำกับ
label_weight = tk.Label(root, text="น้ำหนัก:")
label_weight.place(x=150, y=255)
entry_weight = tk.Entry(root)
entry_weight.place(x=200, y=255)

label_height = tk.Label(root, text="ส่วนสูง:")
label_height.place(x=150, y=294)
entry_height = tk.Entry(root)
entry_height.place(x=200, y=294)

label_age = tk.Label(root, text="อายุ:")
label_age.place(x=150, y=333)
entry_age = tk.Entry(root)
entry_age.place(x=200, y=333)

label_gender = tk.Label(root, text="เพศ:")
label_gender.place(x=150, y=372)
entry_gender = tk.Entry(root)
entry_gender.place(x=200, y=372)

# สร้างปุ่มกด (พื้นหลังสีเขียว)
calculate_button = tk.Button(root, text="คำนวณ", bg="green", fg="white", command=calculate_bmi)
calculate_button.place(x=200, y=410)

# Label แสดงผลลัพธ์
label_result = tk.Label(root, text="ผลลัพธ์:")
label_result.place(x=150, y=450)
result_entry = tk.Entry(root)
result_entry.place(x=200, y=450)

# กำหนดขนาดหน้าจอและแสดง GUI
root.geometry("600x500+420+220")
root.mainloop()
