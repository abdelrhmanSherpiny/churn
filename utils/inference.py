import pandas as pd 
from .CustomerData import CustomerData

def predict_new(data:CustomerData , preprocessor, model):

    df = pd.DataFrame([data.model_dump()])
    X_preprocessed = preprocessor.transform(df)

    y_pred = model.predict(X_preprocessed)
    y_prob = model.predict_proba(X_preprocessed)

    return {
        "Churn_prediction" : bool(y_pred[0]),
        "Churn_probability" : float(y_prob[0][1])
    }