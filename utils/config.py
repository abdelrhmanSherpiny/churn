from dotenv import load_dotenv
import os 
import joblib

load_dotenv(override=True)


APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')
SECRET_KEY_TOKEN = os.getenv('SECRET_KEY_TOKEN')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(BASE_DIR, 'models')

preprocessor = joblib.load(os.path.join(MODELS_DIR, 'preprocessor.pkl'))
forest_model = joblib.load(os.path.join(MODELS_DIR, 'RF_tuned.pkl'))
xgb_model = joblib.load(os.path.join(MODELS_DIR, 'xgb_tuned.pkl'))
