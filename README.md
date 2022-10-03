# Global Shop Stefanini Test
Prueba conocimiento tecnico PYTHON, la aplicación utiliza flask para levantar un servidor en el localHost puerto 5000.

# Requisitos Previos
Necesitara Docker instalado en sus sistema, editor de linea de comandos y Tesseract

```
    Docker
    CMD(Windows)
    Terminal(Linux)
    Tesseract
```

## Installation
Para la instalación se debe descomprimir el archivo ZIP y ejecutar la imagen de Docker:
```
    docker build -t test-stefaniny .
    docker run -d -p 5000:5000 test-stefaniny
```
## Usage
Se adjunto la colección de Api-Rest en Postman, donde existen las siguientes Api Rest:
```
    GET localHost:5000/categorias Devuelve todas las categorias existentes en Mercado Libre del Salvador
    GET localHost:5000/productoGamer Devuelve los productos de la categoria Gamer Mercado Libre Mexico
    GET localHost:5000/textoProducto/id Recibe como parametro de URL el Id de Facebook mencionado en el documento y devulve el texto de la imagen, Id Ejemplo 5681035561916951
    POST localHost:5000/producto Crea documento excel recibiendo por body la URL de la que se quiere extraer los productos para Mercado Libre Salvador
```

## Construido Con
```
    Python
    Flask
    Pytesseract
    Docker
    Pandas
    Pytesseract
    XlsxWriter
```