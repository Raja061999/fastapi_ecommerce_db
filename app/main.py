from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth_router, product_router
from app.db.db_connection import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce API",
    description="An E-commerce application with authentication and product catalog features",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # Or list methods like ["GET", "POST"]
    allow_headers=["*"],  # Or list specific headers
)

# Include Routers
app.include_router(auth_router.router)
app.include_router(product_router.router)