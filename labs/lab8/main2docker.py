
from datetime import datetime
from appJar import gui
from abc import ABC, abstractmethod
import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="calculator_db",
        user="user",
        password="password"
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,            completed BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    print("✓ База данных подключена")
except Exception as e:
    print(f"✗ Ошибка БД: {e}")
    conn = None
    cursor = None


class ToDoAppException(Exception): pass
class TaskNotFoundException(ToDoAppException): pass
class EmptyTaskTitleException(ToDoAppException): pass


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
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.load_tasks()
    
    def add_task(self, title, description=""):
        task = Task(title, description)
        task.id = self.next_id
        self.tasks.append(task)
        self.next_id += 1
        
        if conn:
            try:
                cursor.execute(
                    "INSERT INTO tasks (title, description, completed) VALUES (%s, %s, %s)",
                    (title, description, False)
                )
                conn.commit()
            except Exception as e:
                print(f"Ошибка сохранения в БД: {e}")
        
        return task.id
    
    def remove_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)


                if conn:
                    try:
                        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
                        conn.commit()
                    except Exception as e:
                        print(f"Ошибка удаления из БД: {e}")
                
                return
        raise TaskNotFoundException(f"Задача с ID {task_id} не найдена")
    
    def toggle_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = not task.completed

                
                if conn:
                    try:
                        cursor.execute(
                            "UPDATE tasks SET completed = %s WHERE id = %s",
                            (task.completed, task_id)
                        )
                        conn.commit()
                    except Exception as e:
                        print(f"Ошибка обновления в БД: {e}")
                
                return
        raise TaskNotFoundException(f"Задача с ID {task_id} не найдена")
    
    def get_all_tasks(self):
        return self.tasks.copy()
    
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def load_tasks(self):
        # Загружаем из БД
        if conn:
            try:
                cursor.execute("SELECT id, title, description, completed, created_at FROM tasks ORDER BY id")
                results = cursor.fetchall()
                
                for row in results:
                    task = Task(
                        title=row[1],
                        description=row[2] or "",
                        task_id=row[0],
                        completed=row[3],
                        created_at=row[4]
                    )
                    self.tasks.append(task)
                    
                    if row[0] >= self.next_id:
                        self.next_id = row[0] + 1
                
                print(f"Загружено {len(self.tasks)} задач из БД")
            except Exception as e:
                print(f"Ошибка загрузки из БД: {e}")

# ====================== ПРИЛОЖЕНИЕ ======================
class ToDoApplication:
    def __init__(self):
        self.app = gui("ToDo List", "500x450")
        self.task_manager = TaskManager()
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
        self.app.addButton("История из БД", self.show_db_history, 6, 0, 2)
        
        self.app.addLabel("status", "Готов", 7, 0, 2)
        self.app.setLabelBg("status","#50372c")
        self.app.setLabelFg("status", "white")
        
        self.refresh_list()
    
    def show_db_history(self):
        """Показать все задачи из БД"""
        if conn:
            try:
                cursor.execute("SELECT id, title, description, completed, created_at FROM tasks ORDER BY id DESC LIMIT 10")
                results = cursor.fetchall()
                
                if results:
                    history = "Последние 10 задач из БД:\n\n"
                    for row in results:
                        status = "✓ Выполнена" if row[3] else "○ Не выполнена"
                        history += f"ID:{row[0]} | {row[1]} | {status}\n"
                        history += f"  Описание: {row[2] or 'Нет'}\n"
                        history += f"  Создана: {row[4]}\n"
                        history += "-" * 40 + "\n"
                    self.app.infoBox("История из БД", history)
                else:
                    self.app.infoBox("История", "В БД нет задач")
            except Exception as e:
                self.app.infoBox("Ошибка", f"Ошибка: {e}")
        else:
            self.app.infoBox("Ошибка", "Нет подключения к БД")
    
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
        self.set_status(f"Задача #{task_id} добавлена в БД", "green")
    
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
            self.set_status(f"Задача #{task.id} удалена из БД", "green")
    
    def run(self):
        self.app.go()

# ====================== ЗАПУСК ======================

app = ToDoApplication()
app.run()