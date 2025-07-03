import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันคำนวณ BMI
def calculate_bmi(weight, height_cm, gender):
    try:
        weight = float(weight)
        height_cm = float(height_cm)
        if height_cm <= 0 or weight <= 0:
            raise ValueError("น้ำหนักและส่วนสูงต้องมากกว่า 0")
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return bmi
    except ValueError:
        raise ValueError("กรุณากรอกตัวเลขที่ถูกต้อง")

# ฟังก์ชันแสดงผล BMI พร้อมคำแนะนำ
def show_bmi_result(weight, height_cm):
    gender = gender_var.get()
    if not weight or not height_cm:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกน้ำหนักและส่วนสูงให้ครบ")
        return

    try:
        bmi = calculate_bmi(weight, height_cm, gender)
        result_text = f"ค่า BMI ของคุณคือ: {bmi:.2f}\n"

        # ตีความ BMI
        if gender == "ชาย":
            if bmi < 18.5:
                status = "ผอม"
                advice = "ควรรับประทานอาหารที่มีพลังงานมากขึ้น และออกกำลังกายแบบเพิ่มกล้ามเนื้อ"
            elif bmi < 24.9:
                status = "ปกติ"
                advice = "รักษาน้ำหนักให้คงที่และออกกำลังกายสม่ำเสมอ"
            elif bmi < 29.9:
                status = "น้ำหนักเกิน"
                advice = "ควรระวังอาหารหวาน มัน เค็ม และเพิ่มกิจกรรมทางกาย"
            else:
                status = "อ้วน"
                advice = "ควรควบคุมอาหารและออกกำลังกายอย่างจริงจัง"
        elif gender == "หญิง":
            if bmi < 18.0:
                status = "ผอม"
                advice = "รับประทานอาหารที่มีสารอาหารครบถ้วน และพักผ่อนให้เพียงพอ"
            elif bmi < 23.9:
                status = "ปกติ"
                advice = "ดีมาก! รักษาสุขภาพแบบนี้ต่อไป"
            elif bmi < 28.9:
                status = "น้ำหนักเกิน"
                advice = "ลดปริมาณแป้ง น้ำตาล และเพิ่มการเคลื่อนไหวร่างกาย"
            else:
                status = "อ้วน"
                advice = "ปรึกษาแพทย์หรือนักโภชนาการเพื่อวางแผนลดน้ำหนัก"
        else:
            status = "ไม่สามารถประเมินผลได้"
            advice = "กรุณาเลือกเพศให้ถูกต้อง"

        result_text += f"อยู่ในเกณฑ์: {status}\n"
        result_text += f"คำแนะนำ: {advice}"
        result_label.config(text=result_text)

    except Exception as e:
        messagebox.showerror("ข้อผิดพลาด", str(e))

# กลับไปหน้าเลือกเพศ
def show_gender_page():
    for widget in window.winfo_children():
        widget.destroy()
    build_gender_ui()

# สร้างหน้ากรอกน้ำหนัก/ส่วนสูง
def show_weight_height_page():
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="กรุณาใส่น้ำหนัก (kg):", font=("Arial", 12), bg=bg_color).pack(pady=10)
    weight_entry = tk.Entry(window, font=("Arial", 12))
    weight_entry.pack()

    tk.Label(window, text="กรุณาใส่ส่วนสูง (cm):", font=("Arial", 12), bg=bg_color).pack(pady=10)
    height_entry = tk.Entry(window, font=("Arial", 12))
    height_entry.pack()

    global result_label
    result_label = tk.Label(window, text="", font=("Arial", 12), bg=bg_color, justify="left")
    result_label.pack(pady=10)

    button_frame = tk.Frame(window, bg=bg_color)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="คำนวณ", command=lambda: show_bmi_result(weight_entry.get(), height_entry.get()), bg="#4CAF50", fg="white", font=("Arial", 12)).pack(side="left", padx=10)
    tk.Button(button_frame, text="ย้อนกลับ", command=show_gender_page, bg="#FF7043", fg="white", font=("Arial", 12)).pack(side="left", padx=10)

# สร้างหน้าเลือกเพศ
def build_gender_ui():
    tk.Label(window, text="กรุณาใส่ข้อมูลของคุณ", font=("Arial", 14, "bold"), bg=bg_color).pack(pady=10)
    tk.Label(window, text="เพศ:", font=("Arial", 12), bg=bg_color).pack()

    tk.Radiobutton(window, text="ชาย", variable=gender_var, value="ชาย", font=("Arial", 12), bg=bg_color).pack()
    tk.Radiobutton(window, text="หญิง", variable=gender_var, value="หญิง", font=("Arial", 12), bg=bg_color).pack()

    tk.Button(window, text="ตกลง", command=show_weight_height_page, bg="#2196F3", fg="white", font=("Arial", 12)).pack(pady=20)

# เริ่มต้นหน้าต่างหลัก
window = tk.Tk()
window.title("แอปคำนวณ BMI")
bg_color = "#F0F8FF"
window.configure(bg=bg_color)
window.minsize(width=400, height=450)

# ตัวแปรสำหรับเก็บเพศ
gender_var = tk.StringVar(value="ไม่ระบุ")

# สร้างหน้าแรก
build_gender_ui()
window.mainloop()