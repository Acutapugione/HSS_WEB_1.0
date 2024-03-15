from typing import List
from typing import Optional
from datetime import datetime, date
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .. import Base



class Appeal(Base):
    description: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(13))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(onupdate=datetime.now, nullable=True, )
    #relationships
    target: Mapped["Department"] = relationship(back_populates="appeals")
    executor: Mapped["Executor"] = relationship(back_populates="appeals")
    user: Mapped["User"] = relationship(back_populates="appeals")
    status: Mapped["Status"] = relationship(back_populates="appeal")
    
    #foreign keys
    target_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
    executor_id: Mapped[int] = mapped_column(ForeignKey("executors.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status_id: Mapped[int] = mapped_column(ForeignKey("statuss.id"))

    
    def as_dict(self) -> dict:
        return {
            "№": self.id,
            "Дата створення": self.created_at.strftime("%d.%m.%Y"),
            "Користувач": self.user,
            "Місце проведення": self.target,
            "Виконавець": self.executor,
            "Текст повідомлення": self.description,
            "Статус": self.status,
        }
    def __str__(self) -> str:
        return f"Місце проведення: {self.target}"