from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

# MongoDB connection
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient("mongodb://localhost:27017")
    app.mongodb = app.mongodb_client["mydatabase"]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

# Register routes

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI with MongoDB!"}