import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, auth
from functools import wraps
from streamlit import session_state as state

load_dotenv()

def initialize_firebase():
    cred = credentials.Certificate({
        "type": os.getenv("FIREBASE_TYPE"),
        "project_id": os.getenv("FIREBASE_PROJECT_ID"),
        "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
        "private_key": os.getenv("FIREBASE_PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
        "client_id": os.getenv("FIREBASE_CLIENT_ID"),
        "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
        "token_uri": os.getenv("FIREBASE_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL")
    })
    
    firebase_admin.initialize_app(cred)

initialize_firebase()

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not state.get("user"):
            raise ValueError("Please log in to continue.")
        return func(*args, **kwargs)
    return wrapper

def login(email, password):
    try:
        user = auth.get_user_by_email(email)
        return user
    except Exception as e:
        return None

def signup(email, password):
    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return user
    except Exception as e:
        return None
