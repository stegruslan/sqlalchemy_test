from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

engine = create_engine('sqlite:///test.db')

# Создаем объект сессии
Session = sessionmaker(bind=engine)

# Создаем экземпляр сессии
with Session() as session:
    # Удаляем все таблицы из базы данных
    Base.metadata.drop_all(engine)

print("Таблицы успешно удалены из базы данных.")
