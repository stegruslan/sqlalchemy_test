import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __abstract__ = True


class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(index=True, unique=True)
    description: Mapped[str]
    priority: Mapped[int]
