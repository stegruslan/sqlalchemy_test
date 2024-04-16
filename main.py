from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Task, Base

engine = create_engine('sqlite:///test.db')

session_maker = sessionmaker(bind=engine)

with session_maker() as session:
    Base.metadata.create_all(engine)

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

session.add_all([task1, task2, task3, task4, task5])
session.commit()


priority_input = int(
    input("Введите число приоритета для просмотра задачи от 1 до 3: "))

with session_maker() as session:
    tasks = session.query(Task).filter(
        Task.priority == str(priority_input)).all()

    for task in tasks:
        print("\n"
              f"Задача id={task.id}\n{task.title}\n{task.description}\n"
              f"Приоритет - {task.priority}")
