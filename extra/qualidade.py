import cv2

# Carregar a imagem
imagem = cv2.imread('por.png')

# Verificar a nitidez usando o filtro Laplaciano
imagem_desfocada = cv2.Laplacian(imagem, cv2.CV_64F).var()

# Definir um limiar para a nitidez
limiar_nitidez = 100

if imagem_desfocada > limiar_nitidez:
    print("A imagem parece estar nítida o suficiente.")
else:
    print("A imagem está desfocada e pode afetar o OCR.")
