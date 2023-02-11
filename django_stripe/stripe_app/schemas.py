from pydantic import BaseModel


class ItemBuySchemas(BaseModel):
    name: str
    description: str
    price: int
