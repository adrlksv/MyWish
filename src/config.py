from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()


class Settings(BaseSettings):
    DB_NAME: str
    DB_HOST: str
    DB_PASS: str
    DB_USER: str
    DB_PORT: int
    SECRET_KEY: str
    ALGORITHM: str

    class Config:
        env_file = ".env"

settings = Settings()


# DB_NAME = os.getenv("DB_NAME")
# DB_HOST = os.getenv("DB_HOST")
# DB_PASS = os.getenv("DB_PASS")
# DB_USER = os.getenv("DB_USER")
# DB_PORT = os.getenv("DB_PORT")
# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = os.getenv("ALGORITHM")
