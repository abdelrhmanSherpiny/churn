from fastapi import FastAPI, HTTPException, Depends
from utils.inference import predict_new
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor , forest_model, xgb_model
from utils.CustomerData import CustomerData
from fastapi.security import APIKeyHeader


app = FastAPI(title=APP_NAME,version=VERSION)

@app.get('/', tags= ['General'])
async def home():
    return {
        'message' : f'Welcome to {APP_NAME} API v{VERSION}'
    }

api_key_header = APIKeyHeader(name= "X-API-Key")
async def verify_api_key(api_key: str= Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403, detail="You are not Autharized ti use this API")
    return api_key


@app.post('/predict/forest', tags=['Models'])
async def predict_forest(data:CustomerData,api_key: str= Depends(verify_api_key)) -> dict:
    
    try:
        result = predict_new(data= data, preprocessor= preprocessor, model=forest_model)
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post('/predict/xgboost', tags=['Models'])
async def predict_forest(data:CustomerData,api_key: str= Depends(verify_api_key)) -> dict:
    
    try:
        result = predict_new(data= data, preprocessor= preprocessor, model=xgb_model)
        return result
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
