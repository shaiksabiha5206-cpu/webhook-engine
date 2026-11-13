from pydantic import BaseModel
class WebhookPayload(BaseModel):
    order_id:int
    amount:float
    status:str
    payment_id:int
