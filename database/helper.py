from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine, URL, select, ScalarResult, desc
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from database.models import Base, UrlPath
import os


class DBHelper:
    """
        Class for establishing connection with database
    """
    def __init__(self):
        # load_dotenv()
        self._db_info: dict = {name: value for name, value in os.environ.items() if "DB" in name}
        self._url: URL = URL.create(
            drivername=self._db_info['DB_DRIVERNAME'],
            username=self._db_info['DB_USERNAME'],
            password=self._db_info['DB_PASSWORD'],
            host=self._db_info['DB_HOST'],
            port=self._db_info['DB_PORT'],
            database=self._db_info['DB_DATABASE'],
        )
        self.engine: Engine = create_engine(self._url, echo=True if __debug__ else False)
        self.session: Session = Session(self.engine)
        Base.metadata.create_all(self.engine)

    def add_link(self, url: str, path: str):
        url_path = UrlPath(url=url, s3_path=path)
        try:
            self.session.add(url_path)
            self.session.commit()
        except IntegrityError:
            self.session.rollback()

