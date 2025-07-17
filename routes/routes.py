from fastapi import APIRouter,HTTPException,status,Depends,Form
from typing import Annotated
from model.models import UserRegister,User,UserLogin,Token
from db.database import fake_db
from security.security import hash_password,verify_password
from auth.auth import create_access_token ,get_current_user
from datetime import timedelta

router=APIRouter()

@router.get("/")
def home():
    return {"Message":"Welcome to my User authentication system project"}

@router.post("/register",response_model=User)
def register_user(user:UserRegister):
    if user.username in fake_db:
        raise HTTPException(status_code=400,detail="User already registered")
    fake_db[user.username]={
        "email":user.email,
        "password":hash_password(user.password)
    
    }
    return User(username=user.username,email=user.email)

@router.post("/login", response_model=Token)
def login_user(username: Annotated[str, Form(...,description="Enter your username-",example="John_Doe")], password: Annotated[str, Form(...,description="Enter your password-",example="secure123")]):
    db_user = fake_db.get(username)
    if not db_user or not verify_password(password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": username}, expires_delta=timedelta(minutes=30))
    return Token(access_token=access_token, token_type="bearer")

@router.get("/me",response_model=User)
def read_profile(current_user:User=Depends(get_current_user)):
    return current_user