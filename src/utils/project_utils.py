from datetime import datetime 

from src.config import project_conf 


def get_current_datetime_with_tz() -> datetime:
    return datetime.now(tz=project_conf.current_timezone)
