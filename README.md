# News-Category-Kaggle

This project was developed to solve [New Category Dataset](https://www.kaggle.com/rmisra/news-category-dataset) problem and create a classifier to predict which category is the news:

Some technnologies of Machine Learning and Data Science used:

## Embeddings

- Tf-Idf
- Doc2Vec
- BERT Embedding
- Universal Sentence Encoder

## Models

- Random Forest Classifier
- Logistic Regression
- XGBoost Classifier
- Naive Bayes

## Deep Learning

- Convolutional Neural Network (CNN)
- Long-Short Term Memory (LSTM)
- Gated Recorrent Unit (GRU)

## Model Explainability

- SHAP
- LIME

## API

- FastAPI


### Running

To clone and run this application:

```bash
# Clone this repository
$ git clone https://github.com/BruBel/News-Category

# Go into the repository
$ cd News-Category

# Install dependencies
$ pip install -r requirements.txt

# Go into API repository
$ cd code/api

# Run api
$ uvicorn main:app --host 0.0.0.0 --port 5058
```

Now there are two options:
- Go to http://0.0.0.0:5058/docs#/default/predict_category_predict_post
- Click in "Try it out" and fill in the JSON. Execute.

OR

- In terminal:

curl -X POST "http://0.0.0.0:5058/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"headline\":\"HEADLINEHERE\",\"short_description\":\"SHORTDESCRIPTIONHERE\"}"




