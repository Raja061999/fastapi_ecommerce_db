from sqlalchemy.orm import Session
from app.db.models import Order
from app.db.schemas import OrderCreate
from typing import List

class OrderService:
    @staticmethod
    def create_order(order: OrderCreate, db: Session) -> Order:
        db_order = Order(
            user_id=order.user_id,
            product_id=order.product_id,
            quantity=order.quantity,
            status="Pending"
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order

    @staticmethod
    def get_order(order_id: int, db: Session) -> Order:
        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def list_orders(db: Session) -> List[Order]:
        return db.query(Order).all()