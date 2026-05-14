# todo_app.py
from datetime import datetime
from appJar import gui
from abc import ABC, abstractmethod

class Error(Exception):
    pass

class EmptyError(Error):
    pass

class LongError(Error):
    pass

class View(ABC):
    @abstractmethod
    def show(self, task):
        pass

class SimpleView(View):
    def show(self, task):
        if task.done:
            return f"{task.id}. [✓] {task.name}"
        else:
            return f"{task.id}. [○] {task.name}"

class DateView(View):
    def show(self, task):
        if task.done:
            return f"{task.id}. [✓] {task.name} ({task.date_str})"
        else:
            return f"{task.id}. [○] {task.name} ({task.date_str})"

class Task:
    def __init__(self, name):
        if not name or not name.strip():
            raise EmptyError("Введите название задачи!")
        
        if len(name) > 25:
            raise LongError("Название слишком длинное!")
        
        self._id = None
        self._name = name.strip()
        self.done = False
        self._date = datetime.now()
    
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value    
    
    @property
    def name(self):
        return self._name

    @property
    def date_str(self):
        return self._date.strftime("%d.%m")
    
    def toggle(self):
        self.done = not self.done

class TaskList:
    def __init__(self):
        self._tasks = []
        self._next_id = 1
    
    def add(self, name):
        for t in self._tasks:
            if t.name.lower() == name.lower():
                raise Error(f"Задача '{name}' уже есть!")
        
        task = Task(name)
        task.id = self._next_id
        self._tasks.append(task)
        self._next_id += 1
        return task.id
    
    def delete(self, task_id):
        for i in range(len(self._tasks)):
            if self._tasks[i].id == task_id:
                del self._tasks[i]
                return
    
    def toggle(self, task_id):
        for t in self._tasks:
            if t.id == task_id:
                t.toggle()
                return
    
    def get_all(self):
        return self._tasks

class App:
    def __init__(self):
        self.window = gui("Мои задачи", "450x400")
        self.tasks = TaskList()
        self.view = SimpleView()
        self.setup()
    
    def setup(self):
        self.window.setBg("white")
        
        self.window.addLabel("title", "Мои задачи", 0, 0, 2)
        self.window.setLabelFont("title", size=14, weight="bold")
        
        self.window.addListBox("task_list", [], 1, 0, 2)
        self.window.setListBoxHeight("task_list", 12)
        
        self.window.addLabel("lbl_title", "Название:", 2, 0)
        self.window.addEntry("title_entry", 2, 1)
        
        self.window.addButton("Добавить", self.add, 4, 0)
        self.window.addButton("Выполнено", self.complete, 4, 1)
        self.window.addButton("Удалить", self.delete, 5, 0)
        self.window.addButton("Сменить вид", self.change_view, 5, 1)
        
        self.window.addLabel("status", "Готов", 6, 0, 2)
        self.window.setLabelBg("status", "#2c3e50")
        self.window.setLabelFg("status", "white")
        
        self.update()
    
    def change_view(self):
        if isinstance(self.view, SimpleView):
            self.view = DateView()
        else:
            self.view = SimpleView()
        self.update()
        self.ok()
    
    def error(self, msg):
        self.window.setLabel("status", f"Ошибка: {msg}")
        self.window.setLabelFg("status", "red")
    
    def ok(self):
        self.window.setLabel("status", "Готово!")
        self.window.setLabelFg("status", "lightgreen")
    
    def get_id(self):
        selected = self.window.getListBox("task_list")
        
        if not selected or selected[0] == "Нет задач":
            return None
        
        parts = selected[0].split('.')
        
        if parts and parts[0].isdigit():
            return int(parts[0])
        
        return None
    
    def update(self):
        self.window.clearListBox("task_list")
        tasks = self.tasks.get_all()
        
        if not tasks:
            self.window.addListItem("task_list", "Нет задач")
        else:
            for task in tasks:
                text = self.view.show(task)
                self.window.addListItem("task_list", text)
    
    def add(self):
        name = self.window.getEntry("title_entry")
        
        if not name.strip():
            self.error("Введите название!")
            return
        
        try:
            self.tasks.add(name)
            self.window.setEntry("title_entry", "")
            self.update()
            self.ok()
        except (EmptyError, LongError, Error) as e:
            self.error(str(e))
    
    
    def complete(self):
        tid = self.get_id()
        if not tid:
            self.error("Выберите задачу!")
            return
        
        self.tasks.toggle(tid)
        self.update()
        self.ok()
    
    def delete(self):
        tid = self.get_id()
        if not tid:
            self.error("Выберите задачу!")
            return
        
        if self.window.yesNoBox("Подтверждение", f"Удалить задачу #{tid}?"):
            self.tasks.delete(tid)
            self.update()
            self.ok()
    
    def run(self):
        self.window.go()

app = App()
app.run()