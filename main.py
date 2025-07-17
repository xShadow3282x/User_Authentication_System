from fastapi import FastAPI
from routes.routes import router as auth_router

app = FastAPI(title="FastAPI Auth System")

app.include_router(auth_router)
