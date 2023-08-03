# 1. Library imports
from app.models import IrisSpecies
from app.model  import IrisModel
from fastapi    import FastAPI
from sqlalchemy import create_engine, text
from dotenv     import load_dotenv
import os


model = IrisModel()
app = FastAPI()


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


# ==========================================================================================>

# end-point pour tester.
@app.get('/')
async def index():
    return {'message': 'Hello, stranger !!!'}

# end-point pour la prédiction.
@app.get('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }

# end-point pour insérer les données.
@app.post('/insert')
def endpoint_db(data: dict):
    engine = connect()
    with engine.connect() as con:
        statement = text("""
            INSERT INTO prediction (prediction, probability) VALUES (:prediction, :probability)
        """)
        if len(data) > 1 :
            for i in data:
                con.execute(statement, **i)
        else:
            con.execute(statement, data)



# Appeler la fonction endpoint_db depuis Streamlit.
# endpoint_db(data=({"prediction" : "touk touk toukt touk","probability": 4},))

