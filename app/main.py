from fastapi import FastAPI
from app.routers import memes, images

app = FastAPI()

app.include_router(memes.router)
app.include_router(images.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
