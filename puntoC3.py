import boto3
import os
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client('s3')
bucket_name = os.getenv('BUCKET_NAME')
# Nombre del archivo en S3
file_name = "escudo3.png"
# Ruta local donde se guarda el archivo
path= "/home/destro/operativos/operativos2/escudo3.png"
# Descargar
s3.download_file(bucket_name, file_name, path)


