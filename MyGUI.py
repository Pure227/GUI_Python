import tkinter as tk
from tkinter import ttk, filedialog
import numpy as np


def open_csv():
    file_path = filedialog.askopenfilename(title="Open CSV File", filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        update_treeview(df)

def update_treeview(data):
    # Clear existing data in Treeview
    for item in tree.get_children():
        tree.delete(item)

    # Insert new data into Treeview
    for index, row in data.iterrows():
        tree.insert("", "end", values=row.tolist())

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
    # Convert each element to a string before inserting into the Treeview
    str_row = [str(element) for element in row]
    tree.insert("", "end", values=str_row)

# แสดง Treeview
tree.grid(row=0, column=1, padx=10, pady=10)

# สร้างช่องใส่ข้อมูล 4 ช่อง พร้อมข้อความกำกับ
label_weight = tk.Label(root, text="น้ำหนัก:")
label_weight.grid(row=1, column=0)
entry_weight = tk.Entry(root)
entry_weight.grid(row=1, column=1, pady=10)

label_height = tk.Label(root, text="ส่วนสูง:")
label_height.grid(row=2, column=0)
entry_height = tk.Entry(root)
entry_height.grid(row=2, column=1, pady=10)

label_age = tk.Label(root, text="อายุ:")
label_age.grid(row=3, column=0)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1, pady=10)

label_gender = tk.Label(root, text="เพศ:")
label_gender.grid(row=4, column=0)
entry_gender = tk.Entry(root)
entry_gender.grid(row=4, column=1, pady=10)

# สร้างปุ่มกด (พื้นหลังสีเขียว)
calculate_button = tk.Button(root, text="คำนวณ", bg="green", fg="white")
calculate_button.grid(row=5, column=1, pady=5)

# Label แสดงผลลัพธ์
label_result = tk.Label(root, text="ผลลัพธ์:")
label_result.grid(row=6, column=0)
result_entry = tk.Entry(root)
result_entry.grid(row=6, column=1, pady=10)

# สร้างปุ่มกด (เปิดไฟล์ CSV)
open_csv_button = tk.Button(root, text="Open CSV", command=open_csv)
open_csv_button.grid(row=0, column=2, pady=10)

# กำหนดขนาดหน้าจอและแสดง GUI
root.geometry("460x480+420+220")
root.mainloop()
