from ..database import Database
from ..constants import SQL_DATA
from .service import DataService, Record

data_service = DataService(Database(SQL_DATA, print=True))
