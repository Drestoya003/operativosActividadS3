import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

bucket_name = os.getenv('BUCKET_NAME')

#C,i) Cargar un archivo al bucket
#Archivo
file_path="/home/destro/operativos/escudo.png"

file_name="escudo3.png"

s3=boto3.client("s3")

s3.upload_file(file_path,bucket_name,file_name)
print("Archivo subido con éxito")
