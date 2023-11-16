import warnings, time
from urllib3.exceptions import NotOpenSSLWarning
import requests
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import os, sys
import tweepy
from dotenv import load_dotenv
import urllib.request
from urllib.parse import urlparse

from scraper import scrape_article
from utils import transform_url_imore, get_url, delete_image, download_image, extract_answer, log
from twitter import send_tweet
from ai import create_prompt, generate_text, translate

load_dotenv()
warnings.filterwarnings("ignore", category=UserWarning)
warnings.simplefilter('ignore', NotOpenSSLWarning)

MODE = "AI" # Customizable but it automatically chooses beteeen "AI" or "CLASSIC"

def set_mode(new_mode):
    global MODE
    MODE = new_mode

url = get_url()
article = scrape_article(url)

title = article["title"]
content = article["content"]
image_url = article["image_url"]

download_image(image_url, "image.jpg")

if len(translate(title) + translate(content)) < 274:
    MODE="CLASSIC"
    print("CLASSIC mode enabled")

if MODE == "AI":
    titulo = translate(title)
    contenido = translate(content)
    prompt = create_prompt(titulo, contenido)
    answer = None
    while answer is None or len(answer) > 275:
        response = generate_text(prompt)
        answer = extract_answer(response)

    log(translate(title), image_url, translate(content))
    print("AI -> Answer as follows:")
    print(answer)
    send_tweet(answer, "./image.jpg")

elif MODE == "CLASSIC":
    titulo = translate(title)
    contenido = translate(content)
    answer = "🆕 " + titulo + "\n\n" + contenido
    
    log(titulo, image_url, contenido)
    print("CLASSIC -> Answer as follows:")
    print(answer)
    send_tweet(answer, "./image.jpg")

delete_image("./image.jpg")
MODE = "AI"