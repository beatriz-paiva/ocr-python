import pytesseract
from PIL import Image
import os
import xml.etree.ElementTree as ET

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

dir_path = '/home/beatriz-paiva/Documentos/GitHub/ocr-python/'

path_img = os.path.join(dir_path, 'teste.png')

imagem = Image.open(path_img)

texto = pytesseract.image_to_string(imagem)

root = ET.Element('root')
texto_element = ET.SubElement(root, 'texto')
texto_element.text = texto

path_xml = os.path.join(dir_path, 'texto.xml')
tree = ET.ElementTree(root)
tree.write(path_xml, encoding='utf-8')

print("Texto extraído e salvo em formato XML:", path_xml)
