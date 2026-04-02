from tkinter import *
from tkinter import messagebox, filedialog
from docx import Document
from figure_pkg import *

last_rect_result = ""
last_tri_result = ""
last_trap_result = ""

def calculate_rectangle():
    a = float(rect_a_entry.get())
    b = float(rect_b_entry.get())
    s = rect_area(a, b)
    ri = rect_r_in(a, b)
    ro = rect_r_out(a, b)
    
    text = f"Прямоугольник\nСтороны: {a} и {b}\nПлощадь: {round(s,2)}\n"
    if ri > 0:
        text += f"Радиус вписанной: {round(ri,2)}\n"
    else:
        text += "Вписанной окружности нет\n"
    text += f"Радиус описанной: {round(ro,2)}"
    
    rect_result.set(text)
    global last_rect_result
    last_rect_result = text

def calculate_triangle():
    a = float(tri_a_entry.get())
    b = float(tri_b_entry.get())
    c = float(tri_c_entry.get())
    s = tri_area(a, b, c)
    ri = tri_r_in(a, b, c)
    ro = tri_r_out(a, b, c)
    
    text = f"Треугольник\nСтороны: {a}, {b}, {c}\nПлощадь: {round(s,2)}\n"
    text += f"Радиус вписанной: {round(ri,2)}\n"
    text += f"Радиус описанной: {round(ro,2)}"
    
    tri_result.set(text)
    global last_tri_result
    last_tri_result = text

def calculate_trapezoid():
    a = float(trap_a_entry.get())
    b = float(trap_b_entry.get())
    h = float(trap_h_entry.get())
    s = trap_area(a, b, h)
    
    text = f"Трапеция\nОснования: {a} и {b}\nВысота: {h}\nПлощадь: {round(s,2)}\n"
    text += "Радиусы не рассчитываются"
    
    trap_result.set(text)
    global last_trap_result
    last_trap_result = text

def save_all():
    doc = Document()
    doc.add_heading("Расчёт геометрических фигур", 0)
    doc.add_paragraph(f"\n{last_rect_result}")
    doc.add_paragraph(f"\n{last_tri_result}")
    doc.add_paragraph(f"\n{last_trap_result}")
    
    file_path = filedialog.asksaveasfilename(defaultextension=".docx")
    if file_path:
        doc.save(file_path)
        messagebox.showinfo("!!!","Файл сохранён!")

root = Tk()
root.title("Калькулятор геометрических фигур")
root.geometry("750x500")


left_frame = LabelFrame(root, text="Прямоугольник", font=("Arial", 12, "bold"))
left_frame.pack(side="left", fill="both", expand=False, padx=10, pady = 10)

Label(left_frame, text="Сторона a:").grid(row=0, column=0, pady=10)
rect_a_entry = Entry(left_frame, width=10)
rect_a_entry.grid(row=0, column=1, pady=10)

Label(left_frame, text="Сторона b:").grid(row=1, column=0, pady=10)
rect_b_entry = Entry(left_frame, width=10)
rect_b_entry.grid(row=1, column=1, pady=10)

Button(left_frame, text="Рассчитать",command=calculate_rectangle).grid(row=2, column=0, columnspan=2, padx = 10, pady=10)

rect_result = StringVar()
rect_result.set("Результат")
Label(left_frame, textvariable=rect_result, justify="left",pady=5).grid(row=3, column=0, columnspan=2, pady=10)


center_frame = LabelFrame(root, text="Треугольник", font=("Arial", 12, "bold"))
center_frame.pack(side="left", fill="both", expand=False, padx=10, pady=10)

Label(center_frame, text="Сторона a:").grid(row=0, column=0, pady=5)
tri_a_entry = Entry(center_frame, width=10)
tri_a_entry.grid(row=0, column=1, pady=5)

Label(center_frame, text="Сторона b:").grid(row=1, column=0, pady=5)
tri_b_entry = Entry(center_frame, width=10)
tri_b_entry.grid(row=1, column=1, pady=5)

Label(center_frame, text="Сторона c:").grid(row=2, column=0, pady=5)
tri_c_entry = Entry(center_frame, width=10)
tri_c_entry.grid(row=2, column=1, pady=5)

Button(center_frame, text="Рассчитать", command = calculate_triangle).grid(row=3, column=0,columnspan=2, pady=10)

tri_result = StringVar()
tri_result.set("Результат")
Label(center_frame, textvariable=tri_result,justify='left', pady=5).grid(row=4, column=0,columnspan=2, pady=10)


right_frame = LabelFrame(root, text="Трапеция", font=("Arial", 12, "bold"))
right_frame.pack(side="left", fill="both", expand=False, padx=10, pady=10)

Label(right_frame, text="Основание a:").grid(row=0, column=0, pady=10)
trap_a_entry = Entry(right_frame, width=10)
trap_a_entry.grid(row=0, column=1, pady=10)

Label(right_frame, text="Основание b:").grid(row=1, column=0, pady=10)
trap_b_entry =Entry(right_frame, width=10)
trap_b_entry.grid(row=1, column=1, pady=10)

Label(right_frame, text="Высота h:").grid(row=2, column=0, pady=10)
trap_h_entry = Entry(right_frame, width=10)
trap_h_entry.grid(row=2, column=1, pady=10)

Button(right_frame, text="Рассчитать", command = calculate_trapezoid).grid(row=3, column=0, columnspan=2, pady=10)

trap_result = StringVar()
trap_result.set("Результат")
Label(right_frame, textvariable=trap_result,justify="left", padx=5, pady=5).grid(row=4, column=0, columnspan=2, pady=10)


btn = Button(root, text="Сохранить в Word",command=save_all, font=("Arial", 10, "bold"))
btn.pack(side = RIGHT,pady = 65, padx = 15)

root.mainloop()