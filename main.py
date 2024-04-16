from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Task, Base

engine = create_engine('sqlite:///test.db')
# Здесь создается движок (engine) для работы с базой данных SQLite.
# Он связывается с файлом базы данных test.db.

session_maker = sessionmaker(bind=engine)
# Тут создается объект session_maker,
# который используется для создания сессий SQLAlchemy.
# В данном случае он связывается с созданным ранее движком.

with session_maker() as session:
    Base.metadata.create_all(engine)
# Этот блок создает сессию базы данных.
# И автоматически закрывает ее после выполнения всех операций внутри блока.
# Метод create_all, создает все таблицы,

task1 = Task(
    id=11,
    title="Магазин",
    description="Купить хлеб и молоко",
    priority=1
)
task2 = Task(
    id=12,
    title="Учиться",
    description="Просидеть 3 часа за компом",
    priority=1
)
task3 = Task(
    id=13,
    title="Спорт",
    description="Бегать 2 часа в день",
    priority=2
)
task4 = Task(
    id=14,
    title="Отдых",
    description="Отдыхать 1 час",
    priority=2
)
task5 = Task(
    id=15,
    title="Сон",
    description="Спать не более 8-9 часов",
    priority=3
)
# Создаются объекты задач с различными параметрами.

session.add_all([task1, task2, task3, task4, task5])
session.commit()

# Здесь создаются экземпляры объектов задач,
# (task1, task2, task3, task4, task5),
# с различными значениями id, названия, описания и приоритета.
# Затем эти задачи добавляются в сессию
# и фиксируются в базе данных с помощью метода commit.

priority_input = int(
    input("Введите число приоритета для просмотра задачи от 1 до 3: "))
# ТУт строка запрашивает у пользователя ввод числа приоритета,
# для отображения соответствующих задач.

with session_maker() as session:
    tasks = session.query(Task).filter(
        Task.priority == str(priority_input)).all()

    # Здесь создается новая сессия,
    # в которой выполняется запрос к базе данных.
    # Из базы данных извлекаются все задачи с приоритетом,
    # соответствующим введенному пользователем значению.

    for task in tasks:
        print("\n"
              f"Задача id={task.id}\n{task.title}\n{task.description}\n"
              f"Приоритет - {task.priority}")

# После получения задач с указанным приоритетом они выводятся на экран,
# с помощью цикла for.
# Каждая задача выводится в отдельной строке в формате,
# указанном в строке форматирования.
