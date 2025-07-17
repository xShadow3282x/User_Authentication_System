from datetime import datetime,timedelta,timezone
from jose import jwt,JWTError
from fastapi import HTTPException,Depends,status
from fastapi.security import OAuth2PasswordBearer
from model.models import User
from db.database import fake_db

SECRET_KEY="supersecretkey"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data:dict,expires_delta:timedelta| None=None):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc)+(expires_delta or timedelta(minutes=15))
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def get_current_user(token:str=Depends(oauth2_scheme))->User:
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        if username not in fake_db:
            raise HTTPException(status_code=401,detail="User not found")
        user=fake_db[username]
        return User(username=username,email=user["email"])
    except JWTError:
        raise HTTPException(status_code=401,detail="Invalid or expired token")