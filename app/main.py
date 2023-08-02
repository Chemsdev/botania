# 1. Library imports
from app.models import IrisSpecies
from app.model  import IrisModel
from fastapi    import FastAPI

model = IrisModel()
app = FastAPI()

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




