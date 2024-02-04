from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .. import Base


class Department(Base):
    name: Mapped[str] = mapped_column(unique=True)
    orders: Mapped[List["Order"]] = relationship(back_populates="target")
    