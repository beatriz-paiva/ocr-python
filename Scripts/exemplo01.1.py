from PIL import Image
from pytesseract import * 

# import os
# os.environ['TESSDATA_PREFIX'] = '/usr/share/tesseract-ocr/4.00/tessdata/' 


def extrair_texto_com_idioma(imagem_path, idioma):
    imagem = Image.open(imagem_path)
    texto = pytesseract.image_to_string(imagem, lang=idioma)
    return texto

texto_frances = extrair_texto_com_idioma('por.png', 'eng')
print(texto_frances)
