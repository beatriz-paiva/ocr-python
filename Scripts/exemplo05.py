import pytesseract
from PIL import Image

def extrair_texto_em_ROI(imagem_path, coordenadas_ROI):
    imagem = Image.open(imagem_path)
    ROI = imagem.crop(coordenadas_ROI)
    texto = pytesseract.image_to_string(ROI)
    return texto

ROI_coords = (100, 100, 400, 300)  # Exemplo de coordenadas (esquerda, superior, direita, inferior)
texto_ROI = extrair_texto_em_ROI('teste.png', ROI_coords)
print(texto_ROI)
