from typing import Optional, Union
from pydantic import BaseModel


class IrisSpecies(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


class Prediction(BaseModel):
    id: Optional[int]
    prediction : Optional[str]
    probability : Union[float, None]
