import jwt
from datetime import datetime, timedelta
from typing import Optional
from dotenv import load_dotenv
import os
import bcrypt
from fastapi.security import HTTPAuthorizationCredentials

load_dotenv()

SECRET_KEY = os.getenv("SECRET_TOKEN")
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    print(to_encode)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: HTTPAuthorizationCredentials):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except:
        return False


def encrypt_password(password):
    password_bytes = password.encode('utf-8')

    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(password_bytes, salt)

    return hash_password.decode('utf-8')


def equals_password(password, hash_password):
    password_bytes = password.encode('utf-8')
    hash_password_bytes = hash_password.encode('utf-8')
    u = bcrypt.checkpw(password_bytes, hash_password_bytes)
    return u