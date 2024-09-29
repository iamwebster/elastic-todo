from pydantic_settings import BaseSettings 


class ElasticConfig(BaseSettings):
    ELASTIC_HOST: str = "localhost"
    ELASTIC_PORT: int = 9200
    ELASTIC_USER: str = "elastic"
    ELASTIC_PASSWORD: str = "elastic"

    def get_cred(self) -> dict[str, list | tuple[str, str]]:
        cred = {
            "hosts": [f"{self.ELASTIC_HOST}:{self.ELASTIC_PORT}"],
            "basic_auth": (self.ELASTIC_USER, self.ELASTIC_PASSWORD)
        }
        return cred 
    
    class Config:
        env_file = ".env"
        extra = "allow"


elastic_config = ElasticConfig()
USERS_INDEX = "users"
