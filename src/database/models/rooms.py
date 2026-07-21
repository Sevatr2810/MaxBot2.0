from database.models import BaseModel
from sqlalchemy.orm import mapped_column, Mapped

class Room(BaseModel):
    __tablename__ = "rooms"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    link: Mapped[str]
    name: Mapped[str]