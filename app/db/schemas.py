from pydantic import BaseModel
from typing import Optional


# Schema for creating a new user
class UserCreate(BaseModel):
    username: str
    password: str


# Schema for returning user data in responses
class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


# Schema for creating a new product
class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int


# Schema for returning product data in responses
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    quantity: int

    class Config:
        orm_mode = True


# Schema for creating a new order
class OrderCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int


# Schema for returning order data in responses
class OrderResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    status: str

    class Config:
        orm_mode = True