import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

dir_path = '/home/beatriz-paiva/Documentos/GitHub/ocr-python/'

path_img = os.path.join(dir_path, 'teste.png')

imagem = Image.open(path_img)

texto = pytesseract.image_to_string(imagem)

# print(texto)

path_txt = os.path.join(dir_path, 'texto.txt')

with open(path_txt, 'w') as arquivo_txt:
    arquivo_txt.write(texto)

print("Texto extraído e salvo em:", path_txt)

dados = pytesseract.image_to_data(imagem)

path_dados = os.path.join(dir_path, 'dados.txt')

with open(path_dados, 'w') as arquivo_txt:
    arquivo_txt.write(dados)

print("Texto extraído e salvo em:", path_txt)

coordenadas = pytesseract.image_to_boxes(imagem)

path_coord = os.path.join(dir_path, 'coordenadas.txt')

with open(path_coord, 'w') as arquivo_txt:
    arquivo_txt.write(coordenadas)

print("Texto extraído e salvo em:", path_txt)