from sqlalchemy.orm import Session
from app.db.models import Product
from app.db.schemas import ProductCreate
from typing import List

class ProductService:
    @staticmethod
    def create_product(product: ProductCreate, db: Session) -> Product:
        db_product = Product(
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def list_products(db: Session) -> List[Product]:
        return db.query(Product).all()

    @staticmethod
    def get_product(product_id: int, db: Session) -> Product:
        return db.query(Product).filter(Product.id == product_id).first()