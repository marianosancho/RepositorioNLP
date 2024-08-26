
# Abro primer archivo y lo muestro en pantalla
with open('EJEMPLO DE 8859-15.txt') as archivo: 
    contenido = archivo.read()
print(contenido)

# Abro segundo archivo y los muestro en pantalla
with open('EJEMPLO DE UTF-8.txt', encoding='utf-8') as archivo: 
    
    contenido = archivo.read()
print(contenido)