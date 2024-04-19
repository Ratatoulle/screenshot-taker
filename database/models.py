from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class UrlPath(Base):
    __tablename__ = "url_path"

    url: Mapped[str] = mapped_column(TEXT, primary_key=True)
    s3_path: Mapped[str] = mapped_column(TEXT)
