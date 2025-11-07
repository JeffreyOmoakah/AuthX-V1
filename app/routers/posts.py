from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, utils, database

router = APIRouter()

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed_pw = utils.hash(user.password)
    new_user = models.User(email=user.email, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def get_posts(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post).all()
    return posts