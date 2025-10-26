import boto3
import os
from dotenv import load_dotenv

load_dotenv()

bucket_name = os.getenv('BUCKET_NAME')
local_upload_folder = "/home/destro/operativos/operativos2/subir"  
local_download_folder = "/home/destro/operativos/operativos2/descargas"

s3 = boto3.client('s3')

# ==============================
# SUBIR ARCHIVOS
# ==============================
def upload_files():
    print("subiendo archivos")
    #Creo carpeta si no existe
    if not os.path.exists(local_upload_folder):
        print("Esa carpeta no existe mi rey, espere se la creo")
        os.makedirs(local_upload_folder)
        print("ya se creó")
    #Recorro archivos de la carpeta
    files = os.listdir(local_upload_folder)
    #Recorro los archivos dentro del directorio y subo cada uno
    for filename in files:
        file_path = os.path.join(local_upload_folder, filename)
        s3.upload_file(file_path,bucket_name,filename)
        print(f"Archivo {filename} subido con éxito")
    #Verifico los archivos subidos en el bucket
    print("ya se los subí, mire que si")
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response.get('Contents', []):
        print(f" - {obj['Key']}")
# ==============================
# DESCARGAR ARCHIVOS
# ==============================
def download_files():
    print("descargando archivos")
    #Verifico si la carpeta existe
    if not os.path.exists(local_download_folder):
        print("Esa carpeta no existe mi rey, espere se la creo")
        os.makedirs(local_download_folder)
        print("ya se creó")
    #Descargo los archivos en mi carpeta descargar
    response = s3.list_objects_v2(Bucket=bucket_name)
    for obj in response['Contents']:
        filename=obj['Key']
        local_path = os.path.join(local_download_folder, filename)
        s3.download_file(bucket_name, filename, local_path)
        print(f"Ya le descargué '{filename}'")
    #Verifico si los archivos si se descargaron
    print("Ya se los descargué, mire que si")
    files = os.listdir(local_download_folder)
    if not files:
        print("Mentiras que no le descargué nada")
    for file in files:
        print(file)


#Escoja
if __name__ == "__main__":
    print("1 Subir archivos al bucket")
    print("2 Descargar archivos del bucket")
    option = input("Selecciona una opción (1 o 2): ")

    if option == "1":
        upload_files()
    elif option == "2":
        download_files()
    else:
        print("Eso no se puede profe")
# ============================================
# En conclusión lo que varia si quiero subir varios archivos es que puedo usar las herramientas de programación
# Aprendidas en python para subirlos, como métodos, ciclos y demas
# ============================================
