from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

def connect():
    load_dotenv()
    db_host = os.getenv("DB_HOST")
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_database = os.getenv("DB_DATABASE")
    engine = create_engine(f"mysql://{db_username}:{db_password}@{db_host}/{db_database}")
    return engine

def endpoint_db(data: dict):
    engine = connect()
    with engine.connect() as con:
        statement = text("""
            INSERT INTO prediction (prediction, probability) VALUES (:prediction, :probability)
        """)
        if isinstance(data, dict):
            con.execute(statement, **data)
        elif isinstance(data, list):
            con.execute(statement, *data)
    engine.dispose()

# Appeler la fonction endpoint_db depuis Streamlit.
endpoint_db(data=({"prediction" : "touk touk toukt touk","probability": 4},))
