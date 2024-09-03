<<<<<<< HEAD

# Abro primer archivo y lo muestro en pantalla
with open('EJEMPLO DE 8859-15.txt') as archivo: 
    contenido = archivo.read()
print(contenido)

# Abro segundo archivo y los muestro en pantalla
with open('EJEMPLO DE UTF-8.txt', encoding='utf-8') as archivo: 
    
    contenido = archivo.read()
=======

# Abro primer archivo y lo muestro en pantalla
with open('EJEMPLO DE 8859-15.txt') as archivo: 
    contenido = archivo.read()
print(contenido)

# Abro segundo archivo y los muestro en pantalla
with open('EJEMPLO DE UTF-8.txt', encoding='utf-8') as archivo: 
    
    contenido = archivo.read()
>>>>>>> 849e43c5751005fce0e71de2d9d4b69cbc06b0c0
print(contenido)