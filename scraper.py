import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


from utils import transform_url_imore

def scrape_article(url):
    """
    Función para rastrear un artículo de una URL dada.

    Parámetros:
    url (str): URL del artículo a rastrear.

    Retorna:
    dict: Un diccionario que contiene el título, la URL de la imagen y el contenido del artículo.
    """
    image_url = None
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    except Exception as e:
        return {"error": str(e)}

    if 'macrumors' in url[:25]:
        driver = webdriver.Firefox() 
        driver.get(url)
        time.sleep(5) 
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', class_='heading--1cooZo6n heading--h4--3n5gZUlc heading--white--2vAPsAl1 heading--noMargin--mnRHPAnD')
        image_elements = soup.select('img.size-full')
        content = soup.find('p')

        for image_element in image_elements:
            if 'srcset' in image_element.attrs:
                srcset = image_element['srcset'].split(',')
                srcset.sort(key=lambda x: int(x.split()[-1][:-2]), reverse=True)
                image_url = srcset[0].split()[0]
        driver.quit()
        return {"title": title.text, "image_url": image_url, "content": content.text}


    elif '9to5mac' in url[:25]:
        title = soup.find('h1', class_='h1')
        image_element = soup.find('img', class_='skip-lazy')
        content = soup.find('p')

    elif 'imore' in url[:25]:
        title = soup.find('h1')
        image_element = soup.find('img', class_='block-image-ads hero-image')
        image_element['src'] = transform_url_imore(image_element['src'])
        content = soup.select_one('div.text-copy.bodyCopy.auto p')

    else:
        title = soup.find('h1')
        image_element = soup.select_one('img')
        content = soup.find('p')

    title = title.text if title else 'No title found'
    image_url = image_element['src'] if image_element else 'https://s1.eestatic.com/2019/03/25/actualidad/actualidad_385974370_130494843_1706x960.jpg'
    content = content.text if content else 'No content found'

    return {"title": title, "image_url": image_url, "content": content}