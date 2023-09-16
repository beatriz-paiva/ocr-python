import pytesseract
from pytesseract import TesseractError

try:
    texto_extraido = pytesseract.image_to_string('french.jpg')
    
except TesseractError as e:
    print(f"Ocorreu um erro ao realizar OCR: {e}")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
else:
    print("Texto extraído com sucesso:")
    print(texto_extraido)
