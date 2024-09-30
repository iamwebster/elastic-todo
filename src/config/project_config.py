from datetime import timezone, timedelta

from pydantic_settings import BaseSettings 


class ProjectConfig(BaseSettings):

    @property
    def current_timezone(self):
        return timezone(timedelta(hours=3))


project_conf = ProjectConfig()
