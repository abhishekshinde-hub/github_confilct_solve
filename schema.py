from pydantic import BaseModel

class Product(BaseModel):
    product_id : int
    product_name : str
    product_price : float
    stock : str

class Register(BaseModel):
    username:str
    password:str
    email :str