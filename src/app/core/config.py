import os
# from dotenv import load_dotenv



class Settings:
    def __init__(self):
        # load_dotenv()
        
        PROJECT_NAME:str = "My Application"
        PROJECT_VERSION: str = "V1.0.0"

        POSTGRES_USER : str = os.getenv("POSTGRES_USER", "postgres")
        POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "postgres")
        POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
        POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
        POSTGRES_DB : str = os.getenv("POSTGRES_DB","my_db")
        self.database_url = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    def gino_config(self):
        return {
            "dsn": self.database_url   
        }