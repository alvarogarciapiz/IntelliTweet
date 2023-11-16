import requests
from translate import Translator

def create_prompt(title, content):
    """
    Esta función crea un prompt para generar un tweet basado en una noticia.

    Parámetros:
    title (str): El título de la noticia.
    content (str): El contenido de la noticia.

    Devuelve:
    prompt (str): El prompt para generar el tweet.
    """
    prompt = "Vamos a comunicarnos en español (castellano de España). Al final de este mensaje te voy a compartir una noticia. Empleando un tono profesional e informativo quiero que redactes un resumen de esa noticia en español con un límite de 200 caracteres. Es necesario que incluyas 2 emojis que estén relacionados con la noticia. ESTÁ PROHIBIDO USAR HASHTAGS .Respóndeme en español castellano de ESPAÑA. La noticia tiene este título: " + title + ". Y el cuerpo de la noticia " + content + ". (El id de la respuesta json debe ser \"tweet\"). MUY IMPORTANTE RESPONDER EN ESPAÑOL. ESTÁ PROHIBIDO RESPONDER EN INGLÉS"
    return prompt


def generate_text(prompt):
    """
    Esta función genera un texto basado en un prompt utilizando una API.

    Parámetros:
    prompt (str): El prompt para generar el texto.

    Devuelve:
    response (Response): La respuesta de la API.
    """
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "llama2",
        "prompt": prompt,
        "format": "json",
        "stream": False
    }

    response = requests.post(url, json=data)
    return response

def translate(input):
    """
    Esta función traduce un texto a español.
    Change the "to_lang" parameter to change the language.
    """
    translator = Translator(to_lang="es")
    translation = translator.translate(input)
    return translation