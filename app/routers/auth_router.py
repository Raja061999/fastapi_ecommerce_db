from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.schemas import UserCreate, UserResponse
from app.services.auth_service import AuthService
from app.db.db_connection import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return AuthService.signup(user, db)

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    
    token = AuthService.login(username, password, db)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    return {"access_token": token, "token_type": "bearer"}