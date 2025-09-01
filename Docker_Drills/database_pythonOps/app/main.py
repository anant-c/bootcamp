from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .conf.db import get_db, Base, engine
from .schemas.user_schema import UserSchema
from .models.db_models import User_Try

# Create all tables on application startup
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Your CORS middleware...

@app.get("/get-users", response_model=list[UserSchema])
def read_root(db: Session = Depends(get_db)):
    users = db.query(User_Try).all()
    if not users:
        raise HTTPException(status_code=404, detail="Users not found.")
    return users

@app.post("/post-user", response_model=UserSchema)
def post_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User_Try(
        name=user.name,
        email=user.email,
        age=user.age
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user