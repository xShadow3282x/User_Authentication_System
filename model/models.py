from pydantic import BaseModel,EmailStr,Field
from typing import Annotated
class UserRegister(BaseModel):
    username:Annotated[str,Field(...,description="Enter a unique user name for the registration",example="kingpin70012")]
    email:Annotated[EmailStr,Field(...,description="Enter a valid email",example="abc@gmail.com")]
    password:Annotated[str,Field(...,description="Any unique and strong password")]

class UserLogin(BaseModel):
     username:Annotated[str,Field(...,description="Enter your username for login")]
     password:Annotated[str,Field(...,description="Enter your password for the login authentication")]

class Token(BaseModel):
     access_token:Annotated[str,Field(...)]
     token_type:Annotated[str,Field(...)]= "bearer"

class User(BaseModel):
    username:Annotated[str,Field(...)]
    email:Annotated[EmailStr,Field(...)]
     
