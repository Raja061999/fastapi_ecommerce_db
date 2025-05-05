from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.schemas import OrderCreate, OrderResponse
from app.services.order_service import OrderService
from app.db.db_connection import get_db
from typing import List

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return OrderService.create_order(order, db)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = OrderService.get_order(order_id, db)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found"
        )
    return order

@router.get("/", response_model=List[OrderResponse])
def list_orders(db: Session = Depends(get_db)):
    return OrderService.list_orders(db)