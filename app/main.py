import os
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# MongoDB connection
# Получение значений из переменных окружения
MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")
@app.on_event("startup")
async def startup_db_client():
    print(MONGODB_DB_NAME)
    app.mongodb_client = AsyncIOMotorClient(MONGODB_URL)
    app.mongodb = app.mongodb_client[MONGODB_DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

# Register routes

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB!"}