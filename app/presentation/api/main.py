from fastapi import FastAPI
from app.presentation.di.di import setup_di
from app.presentation.api.routes import router

app = FastAPI()

setup_di(app)
app.include_router(router)