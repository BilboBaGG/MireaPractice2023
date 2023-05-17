import os

HOST = "postgres"
PORT = "5432"
NAME = os.getenv("DB_NAME")
USER =  os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")

DBSTRING = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}"