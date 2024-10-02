from pydantic import BaseModel

# Pydantic model for creating a user
class UserCreate(BaseModel):
    name: str
    email: str

# Pydantic model for reading a user
class UserRead(BaseModel):
    id: int
    name: str
    email: str
