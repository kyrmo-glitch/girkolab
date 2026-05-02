import tkinter as tk
from tkinter import messagebox, filedialog
from abc import ABC, abstractmethod
from docx import Document
from figure_pkg import *

class Figure(ABC):
   
    def __init__(self, name):
        self._name = name
        self._area = 0
        self._result = ""
    
    @property
    def area(self):
        return self._area
    
    @area.setter
    def area(self, value):
        if value < 0:                    
            raise ValueError("Площадь не может быть отрицательной!")
        self._area = value
    
    @abstractmethod
    def calculate(self):
        pass
    
    def __str__(self):
        result = f"{self._name}: {self._result}"
        print(f"[__str__] Вызван у {self._name}")
        print(result)
        return result
    
    def __len__(self):
        length = len(self._result)
        print(f"[__len__] Вызван у {self._name}, длина = {length}")
        return length


class Rectangle(Figure):
    """Класс для прямоугольника"""
    
    def __init__(self):
        super().__init__("Прямоугольник")
        self.a = 0
        self.b = 0
    
    def calculate(self):
        """Расчёт параметров прямоугольника"""
        self.area = rect_area(self.a, self.b)
        ri = rect_r_in(self.a, self.b)
        ro = rect_r_out(self.a, self.b)
        
        self._result = f"Площадь: {round(self.area, 2)}\n"
        if ri > 0:
            self._result += f"Радиус вписанной: {round(ri, 2)}\n"
        else:
            self._result += "Вписанной окружности нет\n"
        self._result += f"Радиус описанной: {round(ro, 2)}"
        return self._result
    
    def __repr__(self):
        """Dunder-метод: вызывается при repr(объект)"""
        print(f"[__repr__] Вызван у Rectangle({self.a}, {self.b})")
        return f"Rectangle({self.a}, {self.b})"
    
    def __add__(self, other):
        if isinstance(other, Figure):
            result = self.area + other.area
            print(f"[__add__] {self.area} + {other.area} = {result}")
            return result
        


class Triangle(Figure):
    """Класс для треугольника"""
    
    def __init__(self):
        super().__init__("Треугольник")
        self.a = 0
        self.b = 0
        self.c = 0
    
    def calculate(self):
        """Расчёт параметров треугольника"""
        self.area = tri_area(self.a, self.b, self.c)
        ri = tri_r_in(self.a, self.b, self.c)
        ro = tri_r_out(self.a, self.b, self.c)
        
        self._result = f"Площадь: {round(self.area, 2)}\n"
        self._result += f"Радиус вписанной: {round(ri, 2)}\n"
        self._result += f"Радиус описанной: {round(ro, 2)}"
        return self._result
    
    def __repr__(self):
        """Dunder-метод: вызывается при repr(объект)"""
        print(f"[__repr__] Вызван у Triangle({self.a}, {self.b}, {self.c})")
        return f"Triangle({self.a}, {self.b}, {self.c})"
    
    def __sub__(self, other):
        """Dunder-метод: вызывается при объект1 - объект2 (разность площадей)"""
        if isinstance(other, Figure):
            result = abs(self.area - other.area)
            print(f"[__sub__] |{self.area} - {other.area}| = {result}")
            return result
        


class Trapezoid(Figure):
    """Класс для трапеции"""
    
    def __init__(self):
        super().__init__("Трапеция")
        self.a = 0
        self.b = 0
        self.h = 0
    
    def calculate(self):
        """Расчёт параметров трапеции"""
        self.area = trap_area(self.a, self.b, self.h)
        ri =  trap_r_in(self.a, self.b, self.h)
        ro =  trap_r_in(self.a, self.b, self.h)
        self._result = f"Площадь: {round(self.area, 2)}\n"
        self._result += f"Радиус вписанной: {round(ri, 2)}\n"
        self._result += f"Радиус вписанной: {round(ro, 2)}\n"
        return self._result
    
    def __repr__(self):
        """Dunder-метод: вызывается при repr(объект)"""
        print(f"[__repr__] Вызван у Trapezoid({self.a}, {self.b}, {self.h})")
        return f"Trapezoid({self.a}, {self.b}, {self.h})"
    
    def __mul__(self, factor):
        """Dunder-метод: вызывается при объект * число (умножение площади)"""
        if isinstance(factor, (int, float)):
            result = self.area * factor
            print(f"[__mul__] {self.area} * {factor} = {result}")
            return result
       

class App:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Калькулятор фигур")
        self.root.geometry("1000x1000")
        
        self.rect = Rectangle()
        self.tri = Triangle()
        self.trap = Trapezoid()
        
        self.setup_ui()
    
    def setup_ui(self):
        """Создание интерфейса"""
        # ===== ПРЯМОУГОЛЬНИК =====
        tk.Label(self.root, text="ПРЯМОУГОЛЬНИК", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Сторона a:").pack()
        self.rect_a = tk.Entry(self.root)
        self.rect_a.pack()
        
        tk.Label(self.root, text="Сторона b:").pack()
        self.rect_b = tk.Entry(self.root)
        self.rect_b.pack()
        
        tk.Button(self.root, text="Рассчитать", command=self.calc_rectangle).pack(pady=5)
        self.rect_result = tk.Label(self.root, text="Результат:", bg="lightgray", relief=tk.SUNKEN)
        self.rect_result.pack(fill=tk.X, padx=20, pady=5)
        
        # ===== ТРЕУГОЛЬНИК =====
        tk.Label(self.root, text="ТРЕУГОЛЬНИК", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Сторона a:").pack()
        self.tri_a = tk.Entry(self.root)
        self.tri_a.pack()
        
        tk.Label(self.root, text="Сторона b:").pack()
        self.tri_b = tk.Entry(self.root)
        self.tri_b.pack()
        
        tk.Label(self.root, text="Сторона c:").pack()
        self.tri_c = tk.Entry(self.root)
        self.tri_c.pack()
        
        tk.Button(self.root, text="Рассчитать", command=self.calc_triangle).pack(pady=5)
        self.tri_result = tk.Label(self.root, text="Результат:", bg="lightgray", relief=tk.SUNKEN)
        self.tri_result.pack(fill=tk.X, padx=20, pady=5)
        
        # ===== ТРАПЕЦИЯ =====
        tk.Label(self.root, text="ТРАПЕЦИЯ", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self.root, text="Основание a:").pack()
        self.trap_a = tk.Entry(self.root)
        self.trap_a.pack()
        
        tk.Label(self.root, text="Основание b:").pack()
        self.trap_b = tk.Entry(self.root)
        self.trap_b.pack()
        
        tk.Label(self.root, text="Высота h:").pack()
        self.trap_h = tk.Entry(self.root)
        self.trap_h.pack()
        
        tk.Button(self.root, text="Рассчитать", command=self.calc_trapezoid).pack(pady=5)
        self.trap_result = tk.Label(self.root, text="Результат:", bg="lightgray", relief=tk.SUNKEN)
        self.trap_result.pack(fill=tk.X, padx=20, pady=5)
        
        # ===== КНОПКА СОХРАНЕНИЯ =====
        tk.Button(self.root, text="Сохранить в Word", command=self.save_to_word, 
                  bg="lightblue", font=("Arial", 12)).pack(pady=20)
    
    def calc_rectangle(self):
        """Обработчик расчёта прямоугольника"""
        self.rect.a = float(self.rect_a.get())
        self.rect.b = float(self.rect_b.get())
        result = self.rect.calculate()
        self.rect_result.config(text=f"Результат:\n{result}")
        
        # Вызов dunder-методов
        print("\n -РЕЗУЛЬТАТ ПРЯМОУГОЛЬНИКА-")
        str(self.rect)
        len(self.rect)
        repr(self.rect)

        if self.rect.area > 0 and self.tri.area > 0 and self.trap.area > 0:
            print("\n" + "-"*50)
            print("ОПЕРАЦИИ С ФИГУРАМИ")
            print("-"*50)
            self.rect + self.tri
            self.tri - self.trap
            self.trap * 3
            
        
    
    def calc_triangle(self):
        """Обработчик расчёта треугольника"""
        self.tri.a = float(self.tri_a.get())
        self.tri.b = float(self.tri_b.get())
        self.tri.c = float(self.tri_c.get())
        result = self.tri.calculate()
        self.tri_result.config(text=f"Результат:\n{result}")
        
        # Вызов dunder-методов
        print("\n -РЕЗУЛЬТАТ ТРЕУГОЛЬНИКА-")
        str(self.tri)
        len(self.tri)
        repr(self.tri)

        if self.rect.area > 0 and self.tri.area > 0 and self.trap.area > 0:
            print("\n" + "-"*50)
            print("ОПЕРАЦИИ С ФИГУРАМИ")
            print("-"*50)
            self.rect + self.tri
            self.tri - self.trap
            self.trap * 2
            self.trap * 3
            
        
    
    def calc_trapezoid(self):
       
        self.trap.a = float(self.trap_a.get())
        self.trap.b = float(self.trap_b.get())
        self.trap.h = float(self.trap_h.get())
        result = self.trap.calculate()
        self.trap_result.config(text=f"Результат:\n{result}")
        
        
        print("\n -РЕЗУЛЬТАТ ТРАПЕЦИИ-")
        str(self.trap)
        len(self.trap)
        repr(self.trap)


        if self.rect.area > 0 and self.tri.area > 0 and self.trap.area > 0:
            print("\n" + "-"*50)
            print("ОПЕРАЦИИ С ФИГУРАМИ")
            print("-"*50)
            self.rect + self.tri
            self.tri - self.trap
            self.trap * 2
            self.trap * 3
        
    def save_to_word(self):
        """Сохранение результатов в Word"""
        doc = Document()
        doc.add_heading("Результаты расчётов", 0)
        
        if self.rect._result:
            doc.add_paragraph(self.rect._result)
        
        if self.tri._result:
            doc.add_paragraph(self.tri._result)
        
        if self.trap._result:
            doc.add_paragraph(self.trap._result)
        
        path = filedialog.asksaveasfilename(
            defaultextension=".docx", 
            initialfile="результаты.docx"
        )
        if path:
            doc.save(path)
            messagebox.showinfo("Успех", "Файл сохранён!")
    
    def run(self):
        self.root.mainloop()

        
app = App()
app.run()

