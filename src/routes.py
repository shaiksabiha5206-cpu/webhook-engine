from fastapi import APIRouter
from schemas import WebhookPayload
from worker import process_webhook
router = APIRouter()
@router.post("/webhook")
def recieve_webhook(payload:WebhookPayload):
    print(f"webhook recieved for order{payload.order_id}")
    process_webhook(payload)
    return{"status":"ok","order_id":payload.order_id}