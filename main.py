
<<<<<<< HEAD
from fastapi import FastAPI,status
from schema import Product,Register
=======
from fastapi import FastAPI,status,HTTPException
from schema import Product,Login
>>>>>>> feature/login

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


userdata = []
@app.post("/register")
def register_user(request:Register):
    data= {
        "username":request.username,
        "password":request.password,
        "email":request.email

    }
    userdata.append(data)
    return userdata

@app.get("/user_data")
def see_user():
    return userdata
userlogin_data = [
    {"username":"abhishek","password":"12345678","email":"sha601021@gmail.com"},
    {"username":"aryan","password":"12345678","email":"aryanshinde@gmail.com"},
    {"username":"yashonir","password":"12345678","email":"yashonir@gmail.com"}
]

@app.post("/login")
def login(request:Login):
    username = request.username
    password = request.password
    for data in userlogin_data:
        if data["username"] == request.username and data["password"] ==request.password:
            return {"message":"Login successfull","user-data":data}
        raise HTTPException(detail="Wrong username or password" ,status_code=status.HTTP_400_BAD_REQUEST)
        
