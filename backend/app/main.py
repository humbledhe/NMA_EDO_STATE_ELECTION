#Third Party
from fastapi import FastAPI
# Local modules


app = FastAPI()

@app.get("/")
def root():
    return {"mesaage": "Hello World"}