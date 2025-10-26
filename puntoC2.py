import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Nombre del bucket
bucket_name = os.getenv('BUCKET_NAME')

s3=boto3.client("s3")
#C,ii) Mostrar que se subió el archivo
response = s3.list_objects_v2(Bucket=bucket_name)

print("Archivos en el bucket:")
for obj in response.get('Contents', []):
    print(f" - {obj['Key']}")

