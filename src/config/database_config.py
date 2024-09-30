from pydantic_settings import BaseSettings 


class ElasticConfig(BaseSettings):
    ELASTIC_HOST: str = "localhost"
    ELASTIC_PORT: int = 9200
    ELASTIC_USER: str = "elastic"
    ELASTIC_PASSWORD: str = "elastic"

    USERS_INDEX = "users"

    def get_cred(self) -> dict[str, list | tuple[str, str]]:
        cred = {
            "hosts": [f"{self.ELASTIC_HOST}:{self.ELASTIC_PORT}"],
            "http_auth": (self.ELASTIC_USER, self.ELASTIC_PASSWORD)
        }
        return cred 
    
    class Config:
        env_file = ".env"
        extra = "allow"


class MysqlConfig(BaseSettings):
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "root"
    MYSQL_DB: str = "elastic_todo"

    def get_url(self):
        return f"""
        mysql+aiomysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}
        @{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DB}
        """


mysql_config = MysqlConfig()
elastic_conf = ElasticConfig()
