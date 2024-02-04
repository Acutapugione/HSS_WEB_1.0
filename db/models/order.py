from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .. import Base


class Order(Base):
    description: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(13))
    
    target: Mapped["Department"] = relationship(back_populates="orders")
    executor: Mapped["Executor"] = relationship(back_populates="orders")
    target_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
    executor_id: Mapped[int] = mapped_column(ForeignKey("executors.id"))
    