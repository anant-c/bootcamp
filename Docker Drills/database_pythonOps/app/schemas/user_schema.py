from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    name: str
    email: str
    age: int