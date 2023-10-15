from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.presentation.di.di import setup_di
from app.presentation.routes import router
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

setup_di(app)
app.mount("/static", StaticFiles(directory="static"))
app.include_router(router)
add_pagination(app)
