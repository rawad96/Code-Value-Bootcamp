

from time import sleep
from fastapi import FastAPI


app = FastAPI()

products = [{
    "id": 1,
    "name": "sfdfsd"
}]

@app.get("/products")
async def get_products():
    return products

@app.get("/hello")
async def hello():
    sleep(10)
    return {"hello": "world"}

@app.get("/add/{x}/{y}")
async def add(x: int, y: int):
    return {"sum": x+y}

@app.get("/multiply")
async def multiply(x: int, y: int):
    return {"total": x*y}

@app.get("/users")
async def get_users():
    pass

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    pass
