from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field


class EventRequest(BaseModel):
    type: str
    origin: Optional[str]
    destination: Optional[str]
    amount: Decimal
