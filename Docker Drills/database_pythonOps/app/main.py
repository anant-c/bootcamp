from fastapi import FastAPI, HTTPException
from conf.db import get_db
from schemas.user_schema import UserSchema
from models.db_models import User_Try

from sqlalchemy.orm import Session


app = FastAPI()


origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "*"
]

@app.get("/get-users")
def read_root(db:Session):
    user = db.query(User_Try).all()

    if not user:
        raise HTTPException(status_code=404, detail=f"Users not found.")

    return {
        "message": "Users fetched successfully.",
        "users": user
    }    

@app.post("/post-user")
def post_user(db: Session, user: UserSchema):
    new_user = User_Try(
        name = user.name,
        email = user.email,
        age = user.age
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User created successfully",
        "user_id": str(new_user.id)
    }
