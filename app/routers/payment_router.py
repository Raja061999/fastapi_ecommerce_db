from fastapi import APIRouter, HTTPException
from app.services.payment_service import PayPalProcessor, StripeProcessor

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

@router.post("/paypal")
def paypal_payment(amount: float):
    processor = PayPalProcessor()
    return {"message": processor.process_payment(amount)}

@router.post("/stripe")
def stripe_payment(amount: float):
    processor = StripeProcessor()
    return {"message": processor.process_payment(amount)}