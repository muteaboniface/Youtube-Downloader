from fastapi import FastAPI
from app.backend.home import root
from app.core.config import settings
from fastapi.staticfiles import StaticFiles


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(root)


