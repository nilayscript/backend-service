from fastapi import FastAPI, Depends
import random
from motor.motor_asyncio import AsyncIOMotorCollection

app = FastAPI()

@app.get("/random-data")
def get_random_data():
    # Generate an array of random data
    return {
        "numbers": [random.randint(1, 100) for _ in range(10)],
        "names": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "cities": ["New York", "London", "Tokyo", "Paris", "Sydney"]
    }

# Optional: Add health check route
@app.get("/health")
def health_check():
    return {"status": "healthy"}
