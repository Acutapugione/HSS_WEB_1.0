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



class Status(Base):
    title: Mapped[str] = mapped_column(String(150), default="Processing")
    appeal: Mapped["Appeal"] = relationship(back_populates="status")