from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    name: str
    email: EmailStr
    age : int