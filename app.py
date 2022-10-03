from flask import Flask, request
from Controller.categorias import Categories
from Controller.producto import Product, Producto_Gamer, Get_Image_Product

app = Flask(__name__)
headers = {'User-Agent':'Mozilla/5.0'}


@app.route("/categorias", methods=['GET'])
def Get_Categories():
    res = Categories(headers)
    return res , 200 if res['hasError'] == False else 400

@app.route("/producto", methods=['POST'])
def Productos():
    req = request.json
    res = Product(headers, req['url'])
    return res , 200 if res['hasError'] == False else 400


@app.route("/productoGamer", methods=['GET'])
def Productos_Gammer():
    res = Producto_Gamer(headers)
    return res , 200 if res['hasError'] == False else 400

@app.route("/textoProducto/<id>", methods=['GET'])
def Get_Text_Image_Product(id):
    res = Get_Image_Product(headers, id)
    return res , 200 if res['hasError'] == False else 400

    
if __name__ == '__main__':
  port = int(5000)
  app.run(debug=True, host='0.0.0.0', port=port)