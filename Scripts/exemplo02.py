import PyPDF2

def ocr_em_pdf(pdf_path):
    pdf = PyPDF2.PdfReader(open(pdf_path, 'rb'))
    texto_total = ""
    for pagina in pdf.pages:
        texto_total += pagina.extract_text()
    return texto_total

texto_pdf = ocr_em_pdf('file-sample.pdf')
print(texto_pdf)
