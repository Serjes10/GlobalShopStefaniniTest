import pandas as pd
import datetime
from PIL import Image
import pytesseract
import io
import requests



def GenerateExcel(name, data):
    try:
        name =name + '_' + str(datetime.datetime.now().microsecond)
        sheet = CrearObjetoExcel(data)
        df = pd.DataFrame(sheet)
        writer = pd.ExcelWriter(name + '.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name=name, index=False)
        writer.save()
        return Recorrer([{ 'codigo': 0, 'descripcion': 'El excel se genero exitosamente' }])
    except:
        return ErrorControlado('Ocurrio un error al generar el excel')
    
def ErrorControlado(error):
    error = {}
    error['hasError'] = True
    error['data'] = {}
    error['errors'] = [{ 'codigo': 5, 'descripcion': 'Ocurrio un error, estamos trabajando para solucionarlo', 'criticidad': 5000 }]
    return error

def Recorrer(data):
    d = {}
    d['hasError'] = False
    d['data'] = data
    d['errors'] = []
    return d


def CrearObjetoExcel(data):
    excel = {}
    key = data[0].keys()
    for k in key:
        row = []
        for d in data:
            row.append(d[k] if d[k] != '' else 'N/A')
        excel[k] = row
    return excel

def Image_Scan(img_tags):
    pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files/Tesseract-OCR/tesseract.exe'
    custom_config = r'--oem 3 --psm 12 '
    img_srcs = [img['src'] if img.has_attr('src') else '-' for img in img_tags]
    data = []
    for count, x in enumerate(img_srcs):
        df1 = {}
        # img_list.append(x)
        df1['imgUrl'] = x
        if x != '-':
            response = requests.get(x)
            img = Image.open(io.BytesIO(response.content))
            text = pytesseract.image_to_string(img, lang="spa+eng", config=custom_config)
            text = text.strip().split('\n\n')
            df1['imageText'] = text
        data.append(df1)
        
    return data