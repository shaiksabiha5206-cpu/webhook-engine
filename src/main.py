from fastapi import FastAPI
from routes import router
app = FastAPI(title="webhook-engine",description="recieves validates and processor webhooks")
app.include_router(router)