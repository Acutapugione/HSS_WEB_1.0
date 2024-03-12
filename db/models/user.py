from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
import flask_login
from .. import Base
from werkzeug.security import check_password_hash, generate_password_hash

class User( Base ):
    id:Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(128))
    def __str__(self) -> str:
        return f"{self.email}"
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

    authenticated: Mapped[bool] = mapped_column(default=False)
    @property 
    def username(self):
        try:
            name, _ = self.email.split("@")
            name  = name.split(".")[0]
            return name
        except:
            return self.email
        
    @username.setter
    def set_username(self, username):
        raise NotImplementedError("Username setter not implemented")
    
    @property
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.email
    @property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated
    @property
    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False