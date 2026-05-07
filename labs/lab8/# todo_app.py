# todo_app.py
from datetime import datetime
from appJar import gui
from abc import ABC, abstractmethod

# ====================== ИСКЛЮЧЕНИЯ ======================
class ToDoAppException(Exception): pass
class TaskNotFoundException(ToDoAppException): pass
class EmptyTaskTitleException(ToDoAppException): pass

# ====================== ХРАНИЛИЩЕ (полиморфизм) ======================
class Storage(ABC):
    @abstractmethod
    def save(self, data): pass
    
    @abstractmethod
    def load(self): pass

class MemoryStorage(Storage):
    def __init__(self):
        self.data = None
    
    def save(self, data):
        self.data = data
    
    def load(self):
        return self.data

# ====================== ЗАДАЧА ======================
class Task:
    def __init__(self, title, description="", task_id=None, completed=False, created_at=None):
        if not title or not title.strip():
            raise EmptyTaskTitleException("Заголовок не может быть пустым")
        
        self.id = task_id
        self.title = title.strip()
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now()
    
    def get_display_text(self):
        status = "✓" if self.completed else "○"
        text = f"{self.id}. [{status}] {self.title}"
        if self.description:
            text += f" - {self.description[:30]}"
        return text

# ====================== МЕНЕДЖЕР ======================
class TaskManager:
    def __init__(self, storage: Storage):
        self.storage = storage
        self.tasks = []
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, title, description=""):
        task = Task(title, description)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        return task.id
    
    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                return
        raise TaskNotFoundException(f"Задача с ID {task_id} не найдена")
    
    def toggle_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed
                self.save_tasks()
                return
        raise TaskNotFoundException(f"Задача с ID {task_id} не найдена")
    
    def get_all_tasks(self):
        return self.tasks.copy()
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def save_tasks(self):
        data = {
            'next_id': self.next_id,
            'tasks': [{'id': t.id, 'title': t.title, 'description': t.description, 
                       'completed': t.completed, 'created_at': t.created_at.isoformat()} 
                      for t in self.tasks]
        }
        self.storage.save(data)
    
    def load_tasks(self):
        data = self.storage.load()
        if not data: 
            return
        
        self.next_id = data.get('next_id', 1)
        for task_data in data.get('tasks', []):
            task = Task(
                task_data['title'],
                task_data.get('description', ''),
                task_data['id'],
                task_data.get('completed', False),
                datetime.fromisoformat(task_data['created_at']) if 'created_at' in task_data else None
            )
            self.tasks.append(task)

# ====================== ПРИЛОЖЕНИЕ ======================
class ToDoApplication:
    def __init__(self):
        self.app = gui("ToDo List", "500x450")
        self.task_manager = TaskManager(MemoryStorage())
        self.setup_ui()
    
    def setup_ui(self):
        self.app.setBg("#f0f0f0")
        
        self.app.addLabel("title", "Список задач", 0, 0, 2)
        self.app.setLabelFont("title", size=14, weight="bold")
        
        self.app.addListBox("task_list", [], 1, 0, 1, 0)
        self.app.setListBoxHeight("task_list", 12)
        
        self.app.addLabel("lbl_title", "Название:", 2, 0)
        self.app.addEntry("title_entry", 2, 1)
        
        self.app.addLabel("lbl_desc", "Описание:", 3, 0)
        self.app.addEntry("desc_entry", 3, 1)
        
        self.app.addButton("Добавить", self.add_task, 4, 0)
        self.app.addButton("Выполнено", self.complete_task, 4, 1)
        self.app.addButton("Удалить", self.delete_task, 5, 0)
        self.app.addButton("Подробнее", self.show_task_details, 5, 1)
        
        self.app.addLabel("status", "Готов", 6, 0, 2)
        self.app.setLabelBg("status", "#2c3e50")
        self.app.setLabelFg("status", "white")
        
        self.refresh_list()
    
    def set_status(self, text, color="green"):
        self.app.setLabel("status", text)
        self.app.setLabelFg("status", color)
    
    def get_selected_task(self):
        selected = self.app.getListBox("task_list")
        if not selected or selected[0] == "Нет задач":
            return None
        
        task_id = int(selected[0].split('.')[0])
        return self.task_manager.get_task_by_id(task_id)
    
    def show_task_details(self):
        task = self.get_selected_task()
        if not task:
            self.set_status("Сначала выберите задачу", "orange")
            return
        
        status_text = "✓ Выполнена" if task.completed else "○ Не выполнена"
        info = f"""
ПОДРОБНАЯ ИНФОРМАЦИЯ:
📌 ID: {task.id}
📝 Заголовок: {task.title}
📄 Описание: {task.description or 'Нет описания'}
✅ Статус: {status_text}
📅 Дата: {task.created_at.strftime('%d.%m.%Y')}
🕐 Время: {task.created_at.strftime('%H:%M:%S')}
"""
        self.app.infoBox("Детали задачи", info)
    
    def refresh_list(self):
        self.app.clearListBox("task_list")
        tasks = self.task_manager.get_all_tasks()
        
        if not tasks:
            self.app.addListItem("task_list", "Нет задач")
        else:
            for task in tasks:
                self.app.addListItem("task_list", task.get_display_text())
    
    def add_task(self):
        title = self.app.getEntry("title_entry")
        desc = self.app.getEntry("desc_entry")
        
        if not title or not title.strip():
            self.set_status("Ошибка: Заголовок не может быть пустым", "red")
            return
        
        task_id = self.task_manager.add_task(title, desc)
        self.app.setEntry("title_entry", "")
        self.app.setEntry("desc_entry", "")
        self.refresh_list()
        self.set_status(f"Задача #{task_id} добавлена", "green")
    
    def complete_task(self):
        task = self.get_selected_task()
        if not task:
            self.set_status("Выберите задачу", "orange")
            return
        
        self.task_manager.toggle_complete(task.id)
        self.refresh_list()
        self.set_status(f"Статус задачи #{task.id} изменен", "green")
    
    def delete_task(self):
        task = self.get_selected_task()
        if not task:
            self.set_status("Выберите задачу", "orange")
            return
        
        if self.app.yesNoBox("Подтверждение", f"Удалить задачу #{task.id}?"):
            self.task_manager.remove_task(task.id)
            self.refresh_list()
            self.set_status(f"Задача #{task.id} удалена", "green")
    
    def run(self):
        self.app.go()

# ====================== ЗАПУСК ======================
if __name__ == "__main__":
    app = ToDoApplication()
    app.run()