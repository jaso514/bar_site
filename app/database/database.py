# app/database/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
import logging
import config

logger = logging.getLogger(__name__)

Base = declarative_base()

class Database:
    def __init__(self, db_url: str = None):
        if db_url is None:
            db_url = config.DATABASE_URL  # Obtiene la URL desde el archivo de configuración
        self._engine = self._create_engine(db_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)

    def _create_engine(self, db_url: str):
        try:
            engine = create_engine(db_url)
            # Puedes agregar opciones de pooling aquí si es necesario
            # Ejemplo:
            # engine = create_engine(db_url, pool_size=5, max_overflow=10)
            engine.connect()  # Intenta establecer una conexión para verificar
            logger.info("Motor de base de datos creado exitosamente.")
            return engine
        except SQLAlchemyError as e:
            logger.error(f"Error al crear el motor de la base de datos: {e}")
            raise

    def create_all_tables(self):
        try:
            Base.metadata.create_all(bind=self._engine)
            logger.info("Tablas de la base de datos creadas exitosamente.")
        except SQLAlchemyError as e:
            logger.error(f"Error al crear las tablas de la base de datos: {e}")
            raise

    def get_session(self) -> Session:
        """Obtiene una nueva sesión de base de datos."""
        return self.SessionLocal()

    def close_session(self, session: Session):
        """Cierra una sesión de base de datos."""
        session.close()

    # Sugerencia de mejora: Context Manager para la sesión
    def __enter__(self):
        self.session = self.get_session()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.session.rollback()
        else:
            self.session.commit()
        self.close_session(self.session)

# Inicializa la instancia de la base de datos (esto se puede hacer en tu main.py o donde inicies la app)
database = Database()
engine = database._engine
SessionLocal = database.SessionLocal
get_db = database.get_session # Puedes mantener esta variable para compatibilidad hacia atrás

# Ejemplo de cómo crear las tablas
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    database.create_all_tables()