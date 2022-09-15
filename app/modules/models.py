from sqlmodel import SQLModel, Field


class Products(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, nullable=False)