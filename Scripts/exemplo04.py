import cv2
import pytesseract

def ocr_com_preprocessamento(imagem_path):

    imagem_original = cv2.imread(imagem_path)

    imagem_cinza = cv2.cvtColor(imagem_original, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Imagem Cinza", imagem_cinza)
    cv2.waitKey(0)

    # Aplica a binarização
    imagem_binaria = cv2.threshold(imagem_cinza, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("Imagem Binarizada", imagem_binaria)
    cv2.waitKey(0)

    
    texto = pytesseract.image_to_string(imagem_binaria)
    return texto

texto_preprocessado = ocr_com_preprocessamento('/home/beatriz-paiva/Documentos/GitHub/ocr-python/teste.png')
print(texto_preprocessado)
