from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import time
import uuid
from datetime import datetime


app = FastAPI(title="orders-service", version="1.0")

class OrderRequest(BaseModel):
    customerId: Optional[str] = "CUST-001"
    items: Optional[List[Dict[str, Any]]] = [{"sku": "SKU-123", "qty": 1}]
    currency: Optional[str] = "CAD"
    note: Optional[str] = "demo order"

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/ready")
def ready():
    return {"ready": True}

@app.post("/orders")
def create_order(req: OrderRequest):
    order_id = str(time.time() * 1000)
    now = datetime.now()
    formatted_time = now.strftime("%I:%M %p")
    return {
        "orderId": order_id,
        "status": "ACCEPTED",
        "createdAt": formatted_time,
        "summary": {
            "customerId": req.customerId,
            "itemCount": sum([i.get("qty", 0) for i in req.items]),
            "currency": req.currency
        },
        "details": {
            "items": req.items,
            "note": req.note
        }
    }