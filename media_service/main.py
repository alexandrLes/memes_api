from fastapi import FastAPI, File, UploadFile
from minio import Minio
import os

app = FastAPI()

minio_client = Minio(
    endpoint=os.getenv("MINIO_URL").replace("http://", ""),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

@app.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    file_name = file.filename
    content = await file.read()
    minio_client.put_object(
        "memes",
        file_name,
        data=content,
        length=len(content),
        content_type=file.content_type
    )
    return {"url": f"{os.getenv('MINIO_URL')}/memes/{file_name}"}
