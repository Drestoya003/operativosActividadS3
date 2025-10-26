# Para instalar dependencias

# Para iniciar el servicio
# uvicorn main:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
import boto3
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3')
bucket_name = os.getenv('BUCKET_NAME')

# Contador
item_counter = 0

app = FastAPI()

class Item(BaseModel): # BaseModel es una clase que nos va permitir validar el envío de datos por POST
    name: str = 'Mateo'
    description: str = 'Testing'
    price: float = 2000.35


# endpoint: el punto al cual yo quiero llamar de nuestra API
@app.get("/")
def read_root():
    return {"message": "Universidad EIA"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query: str = None):
    return {"item_id": item_id, "query": query}

@app.post("/items/")
def create_item(item: Item):
    global item_counter
    item_counter += 1
    
    record = {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "timestamp": datetime.now().isoformat()
    }
    
    # se genera el archivo
    filename = f"item{item_counter}.json"
    
    # se guarda en s3
    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=json.dumps(record, indent=2),
        ContentType='application/json'
    )
    return {"message": "Se guardó el archivo", "filename": filename}

