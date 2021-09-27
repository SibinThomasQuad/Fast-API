from typing import Optional
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import data
app = FastAPI()
@app.get("/insert")
def insert_contact():
    data.insert_employee()
    return {"status": "true", "message": 'created'}
@app.get("/")
def read_root():
    ResultSet=data.Contactinfo()
    json_compatible_item_data = jsonable_encoder(ResultSet)
    return json_compatible_item_data
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
