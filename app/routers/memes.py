from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas, dependencies

router = APIRouter(
    prefix="/memes",
    tags=["memes"]
)

@router.get("/", response_model=list[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes

@router.get("/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, db: Session = Depends(dependencies.get_db)):
    db_meme = crud.get_meme(db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme

@router.post("/", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_meme(db=db, meme=meme)

@router.put("/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(dependencies.get_db)):
    db_meme = crud.update_meme(db=db, meme_id=meme_id, meme=meme)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme

@router.delete("/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(dependencies.get_db)):
    db_meme = crud.delete_meme(db=db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme
