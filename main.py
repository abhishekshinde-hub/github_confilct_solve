
from fastapi import FastAPI,status
from schema import Product

app = FastAPI()
Product_data = []
@app.post("/addproduct")
def create_product(request:Product,status_code = status.HTTP_201_CREATED):
    print(request)
    data={
   "product_id" : request.product_id,
   "product_name": request.product_name,
   "product_price" : request.product_price,
   "product_stock" : request.product_name
    }
    Product_data.append(data)
    
    return {"Product_data":Product_data}
print(Product_data)

@app.get("/products")
def get_product(status_code = status.HTTP_200_OK):
    return {"data":Product_data,"message":"data has been fethed successfully"}
