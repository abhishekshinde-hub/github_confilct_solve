from pydantic import BaseModel

class Product(BaseModel):
    product_id : int
    product_name : str
    product_price : float
    stock : str
