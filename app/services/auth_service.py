from sqlalchemy.orm import Session
from app.db.models import User
from app.db.schemas import UserCreate
from app.utils.security import hash_password, verify_password, create_access_token

class AuthService:
    @staticmethod
    def signup(user: UserCreate, db: Session) -> User:
        hashed_pwd = hash_password(user.password)
        db_user = User(username=user.username, hashed_password=hashed_pwd)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    @staticmethod
    def login(username: str, password: str, db: Session) -> str:
        db_user = db.query(User).filter(User.username == username).first()
        if not db_user or not verify_password(password, db_user.hashed_password):
            return None
        return create_access_token({"sub": db_user.username})