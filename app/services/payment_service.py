from app.interfaces.payment_processor import PaymentProcessor

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Payment of ${amount} processed using PayPal."

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> str:
        return f"Payment of ${amount} processed using Stripe."