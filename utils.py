import sys
import os
import requests
import json

def transform_url_imore(url):
    return url.replace("320-80.jpg", "650-80.jpg")

def get_url():
    """
    Esta función obtiene la URL de la noticia a partir de los argumentos de la línea de comandos.
    """
    url = sys.argv[1] if len(sys.argv) > 1 else None
    if url is None:
        print("No URL provided")
        exit(1)
    return url

def delete_image(image_path):
    """
    Esta función elimina una imagen.
    """
    os.remove(image_path)

def download_image(image_url, file_path):
    """
    Esta función descarga una imagen.
    """
    response = requests.get(image_url, stream=True)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192): 
            file.write(chunk)


def extract_answer(response):
    """
    Esta función extrae la respuesta de una petición a la API.
    """
    response_json = json.loads(response.text)
    response_data = json.loads(response_json["response"])
    message_names = ['message', 'tweet', 'twitter', 'text', 'Título', 'response']
    for name in message_names:
        if name in response_data:
            return response_data[name]
    print("No se encontró el mensaje en la respuesta.")
    return None

def log(title, image_url, content):
    """
    Esta función imprime en la consola los datos de una noticia.
    """
    print("| ----> IMAGE URL: " + image_url)
    print("| ----> TITLE: " + title )
    print("| ----> CONTENT: " + content )