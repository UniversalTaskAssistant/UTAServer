# app/api/v1/api.py
from fastapi import APIRouter
from .endpoints import automation_routes, user_routes, data_routes

api_router = APIRouter()
api_router.include_router(automation_routes.router, tags=["automation"])
api_router.include_router(user_routes.router, tags=["user"])
api_router.include_router(data_routes.router, tags=["data"])