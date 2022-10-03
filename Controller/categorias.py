import requests
from bs4 import BeautifulSoup
from Utils.Util import Recorrer, ErrorControlado


def Categories(headers):
    try:
        URL = "https://www.mercadolibre.com.sv/categorias#nav-header"
        r = requests.get(url=URL, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')
        categorias = []
        div = soup.find_all('div',class_='categories__container')
        for c in div:
            d = {}
            subCategoria = []
            for h in c.find_all('a',class_='categories__subtitle'):
                s = {}
                s['categoria'] = h.string
                s['url'] = h['href']
                subCategoria.append(s)
                d['categoria'] = c.h2.a.string
                d['url'] = c.h2.a['href']
                d['subCategoria'] = subCategoria
                categorias.append(d)
        return Recorrer(categorias)
    except:
        return ErrorControlado('Ocurrio un error al obtener las categorias')

   
