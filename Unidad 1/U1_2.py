"""
 El Ministerio de Turismo y Deportes de la Nación permite explorar
tableros de información en línea tableros.yvera.tur.ar. 
 
 Explore la página y utilizando una librería de web scraping extraiga los valores del tablero de indicadores de
Objetivos de Desarrollo Sostenible en una tabla y el texto limpio de la metodología
de los mismos. 

"""

import requests
from bs4 import BeautifulSoup

url  = "https://tableros.yvera.tur.ar"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Localizo que lo que busco se encuentra en 