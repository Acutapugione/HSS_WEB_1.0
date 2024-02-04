from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column


engine = create_engine("sqlite:///my_db.db", echo=True)
Session = sessionmaker(engine)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        if hasattr(self, "name"):
            return self.name
        return super().__str__()
    
    @classmethod
    @property
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

from . models import Department, Executor, Order


def up():
    with Session.begin() as session:
        departaments = [
            Department(
                name="Хірургія",
            ),
            Department(
                name="Травматологія"
            ),
            Department(
                name="Гінекологія"
            ),
        ]
        executors = [
            Executor(
                name="Служба Енергетики"
            ),
            Executor(
                name="Будівельна служба"
            ),
        ]
        session.add_all([*departaments, *executors])
        
        

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
up()
