import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables de entorno desde el archivo .env

DATABASE_HOST = os.getenv("MYSQL_HOST", "DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT", "3306")
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_URL = os.getenv(
        "DATABASE_URL",
        f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")

# Construye la cadena de conexión para MySQL Connector/Python
#DATABASE_URL = f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"