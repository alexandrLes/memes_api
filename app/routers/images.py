from fastapi import APIRouter, UploadFile, File, HTTPException
from minio import Minio
import os
from starlette.responses import JSONResponse

router = APIRouter(
    prefix="/images",
    tags=["images"]
)

minio_client = Minio(
    endpoint=os.getenv("MINIO_URL").replace("http://", ""),
    access_key=os.getenv("MINIO_ACCESS_KEY"),
    secret_key=os.getenv("MINIO_SECRET_KEY"),
    secure=False
)

@router.post("/upload")
async def upload_image(file: UploadFile = File(...)):
    bucket_name = "memes"
    
    if not minio_client.bucket_exists(bucket_name):
        minio_client.make_bucket(bucket_name)

    file_name = file.filename
    content = await file.read()
    minio_client.put_object(
        bucket_name,
        file_name,
        data=content,
        length=len(content),
        content_type=file.content_type
    )
    
    file_url = f"{os.getenv('MINIO_URL')}/{bucket_name}/{file_name}"
    return JSONResponse(content={"url": file_url})
