from datetime import datetime
from appJar import gui

class TaskError(Exception):
    pass

class EmptyTitleError(TaskError):
    pass

class TaskTooLongError(TaskError):
    pass

class Task:
    MAX_LENGTH = 30  
    
    def __init__(self, title):
        if not title or not title.strip():
            raise EmptyTitleError("Заголовок не может быть пустым")
        
        if len(title.strip()) > self.MAX_LENGTH:
            raise TaskTooLongError("Название слишком длинное")
        
        self.id = None
        self.title = title.strip()
        self.completed = False
        self.date = datetime.now()
    
    def toggle(self):
        self.completed = not self.completed
    
    def get_text(self):
        status = "✓" if self.completed else "○"
        return f"{self.id}. [{status}] {self.title}"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
    
    def add(self, title):
        for t in self.tasks:
            if t.title.lower() == title.lower():
                raise TaskError(f"Задача '{title}' уже есть")
        
        task = Task(title)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        return task.id
    
    def delete(self, task_id):
        for i, t in enumerate(self.tasks):
            if t.id == task_id:
                del self.tasks[i]
                return
    
    def toggle(self, task_id):
        for t in self.tasks:
            if t.id == task_id:
                t.toggle()
                return
    
    def get_all(self):
        return self.tasks.copy()

class ToDoApp:
    def __init__(self):
        self.app = gui("ToDo List", "450x400")
        self.manager = TaskManager()
        self.setup()
    
    def setup(self):
        self.app.setBg("#f0f0f0")
        
        self.app.addLabel("title", "Мои задачи", 0, 0, 2)
        self.app.setLabelFont("title", size=14, weight="bold")
        
        self.app.addListBox("task_list", [], 1, 0, 2)
        self.app.setListBoxHeight("task_list", 12)
        
        self.app.addLabel("lbl_title", "Название:", 2, 0)
        self.app.addEntry("title_entry", 2, 1)
        
        self.app.addButton("Добавить", self.add_task, 3, 0)
        self.app.addButton("Выполнено", self.complete_task, 3, 1)
        self.app.addButton("Удалить", self.delete_task, 4, 0)
        
        self.app.addLabel("status", "Готов", 5, 0, 2)
        self.app.setLabelBg("status", "#2c3e50")
        self.app.setLabelFg("status", "white")
        
        self.refresh()
    
    def error(self, msg):
        self.app.setLabel("status", f"Ошибка: {msg}")
        self.app.setLabelFg("status", "red")
    
    def ok(self):
        self.app.setLabel("status", "Готов")
        self.app.setLabelFg("status", "white")
    
    def get_selected_id(self):
        selected = self.app.getListBox("task_list")
        if not selected or selected[0] == "Нет задач":
            return None
        try:
            return int(selected[0].split('.')[0])
        except:
            return None
    
    def refresh(self):
        self.app.clearListBox("task_list")
        tasks = self.manager.get_all()
        if not tasks:
            self.app.addListItem("task_list", "Нет задач")
        else:
            for task in tasks:
                self.app.addListItem("task_list", task.get_text())
    
    def add_task(self):
        title = self.app.getEntry("title_entry")
        
        if not title.strip():
            self.error("Введите название")
            return
        
        try:
            self.manager.add(title)
            self.app.setEntry("title_entry", "")
            self.refresh()
            self.ok()
        except EmptyTitleError as e:
            self.error(str(e))
        except TaskTooLongError as e:
            self.error(str(e))
        except TaskError as e:
            self.error(str(e))
    
    def complete_task(self):
        tid = self.get_selected_id()
        if not tid:
            self.error("Выберите задачу")
            return
        
        self.manager.toggle(tid)
        self.refresh()
        self.ok()
    
    def delete_task(self):
        tid = self.get_selected_id()
        if not tid:
            self.error("Выберите задачу")
            return
        
        if self.app.yesNoBox("Удаление", f"Удалить задачу {tid}?"):
            self.manager.delete(tid)
            self.refresh()
            self.ok()
    
    def run(self):
        self.app.go()

app = ToDoApp()
app.run()