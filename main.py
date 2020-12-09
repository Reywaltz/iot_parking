from fastapi import FastAPI
from fastapi import APIRouter
from app.apps.api.routes.route import create_routes, router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_routes()

app.include_router(router)