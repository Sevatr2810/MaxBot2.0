from database.models import BaseModel
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import BigInteger
from datetime import date

class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    max_id: Mapped[int] = mapped_column(BigInteger, unique=True)

    first_name: Mapped[str]
    last_name: Mapped[str]

    birthday: Mapped[date]

    isAdmin: Mapped[bool] = mapped_column(default=False)
    access_level: Mapped[int] = mapped_column(default=0)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"