<<<<<<< HEAD
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

=======
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

>>>>>>> 849e43c5751005fce0e71de2d9d4b69cbc06b0c0
# Localizo que lo que busco se encuentra en 