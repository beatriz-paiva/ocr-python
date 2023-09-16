import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

dir_path = '/home/beatriz-paiva/Documentos/GitHub/ocr-python/'

path_img = os.path.join(dir_path, 'teste.png')

imagem = Image.open(path_img)

texto_extraido = pytesseract.image_to_string(imagem)

path_txt = os.path.join(dir_path, 'texto_extraido.txt')

with open(path_txt, 'w') as arquivo_txt:
    arquivo_txt.write(texto_extraido)

print("Texto extraído e salvo em:", path_txt)
