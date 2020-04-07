from fastapi import FastAPI
from pydantic import BaseModel
from classifier import Classifier

app = FastAPI()


class New(BaseModel):
    headline: str
    short_description: str


class ResponseModel(BaseModel):
    category: str
    proba: float


@app.get('/')
def root():

    return {"message": "Hello World!"}


@app.post('/predict')
async def predict_category(new: New):

    response = Classifier().predict(new.headline, new.short_description)

    response_model = ResponseModel(
        category=response['category'], proba=response['probability'])

    return response_model
