# pip install "fastapi[standard]"
# fastapi dev fastapi_hello_world.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return "Hello world"