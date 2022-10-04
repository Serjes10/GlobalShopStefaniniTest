import requests
from bs4 import BeautifulSoup
from Utils.Util import ErrorControlado, GenerateExcel, Image_Scan, Recorrer

login_basic_url = 'https://mbasic.facebook.com/login'
login_mobile_url = 'https://m.facebook.com/login'

def Product(headers, enlace):
    try:
        request = requests.get(url=enlace, headers=headers)
        soup = BeautifulSoup(request.content, 'lxml')
        productos = []
        for i in soup.find_all('li', class_='ui-search-layout__item shops__layout-item'):
            p ={}
            for d in i.find_all('div',class_='ui-search-result__content-wrapper shops__result-content-wrapper'):
                nombreProducto = d.find('h2', class_='ui-search-item__title shops__item-title')
                simbolo = d.find('span', class_='price-tag-symbol')
                precio = d.find('span', class_='price-tag-fraction')
                p['nombreProducto'] = nombreProducto.string
                p['precio'] = simbolo.string + precio.string
                p['precioOferta'] = ''
                p['sku'] = ''

            productos.append(p)
        return GenerateExcel('Productos',productos)
    except ValueError:
        # print(ValueError)
        return ErrorControlado('Ocurrio un error al consumir los productos')


def Producto_Gamer(headers):
    try:
        enlace = "https://ofertas.mercadolibre.com.mx/flagship-computo-gaming#deal_print_id=3d493430-41e4-11ed-8e49-75885d2b7eae&c_id=special-normal&c_element_order=2&c_campaign=GAMING&c_uid=3d493430-41e4-11ed-8e49-75885d2b7eae"
        request = requests.get(url=enlace, headers=headers)
        soup = BeautifulSoup(request.content, 'lxml')
        productos = []
        for i in soup.find_all('li', class_='ui-search-layout__item'):
            p ={}
            for d in i.find_all('div',class_='ui-search-result__content-wrapper shops__result-content-wrapper'):
                nombreProducto = d.find('h2', class_='ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title')
                oferta = d.find('s', class_='price-tag ui-search-price__part ui-search-price__original-value shops__price-part price-tag__disabled')
                original = d.find('span', class_='price-tag ui-search-price__part shops__price-part') 
                p['nombreProducto'] = nombreProducto.string
                p['precioOriginal'] = oferta.find('span', class_='price-tag-symbol').string + oferta.find('span', class_='price-tag-fraction').string if oferta is not None else ''
                p['precioOferta'] = original.find('span', class_='price-tag-symbol').string + original.find('span', class_='price-tag-fraction').string
                p['sku'] = ''

            productos.append(p)
        return GenerateExcel('Productos_Gamer',productos)
    except:
        return ErrorControlado('Ocurrio un error al consumir los productos')

        
def Get_Image_Product(headers,id):
    try:
        enlace = f'https://mbasic.facebook.com/story.php?story_fbid={id}&id={id}'
        request = requests.get(url=enlace, headers=headers)
        soup = BeautifulSoup(request.content,'html.parser')
        img = soup.find_all('img', class_="o")
        data = Image_Scan(img)  
        return Recorrer(data)  
    except:
        return ErrorControlado('Ocurrio un error interno al obtener el texto de la imagen')

   
    