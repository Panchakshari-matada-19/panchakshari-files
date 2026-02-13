import fitz  # PyMuPDF

pdf_path = r"E:\Python-tutorials\Files\results.pdf" #r -> raw string  

doc = fitz.open(pdf_path)

print("Total Pages:", doc.page_count)

