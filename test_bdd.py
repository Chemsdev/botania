import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def connect():
    
    # Charger les variables d'environnement depuis le fichier .env
    load_dotenv()
    db_host     = os.getenv("DB_HOST")
    db_username = os.getenv("DB_USERNAME")
    db_password = os.getenv("DB_PASSWORD")
    db_database = os.getenv("DB_DATABASE")
    
    # Construire l'URL de connexion MySQL
    engine = create_engine(f"mysql://{db_username}:{db_password}@{db_host}/{db_database}")
    return engine

def endpoint_db(data: dict):
    engine = connect()
    with engine.connect() as con:
        statement = text("""
            INSERT INTO botania_prediction (prediction, probability) VALUES (:prediction, :probability)
        """)
        if len(data) > 1 :
            for i in data:
                con.execute(statement, **i)
        else:
            con.execute(statement, data)


# Appeler la fonction endpoint_db depuis Streamlit.
endpoint_db(data=({"prediction" : "ta pas 2 balles","probability": 4},))

# a faire