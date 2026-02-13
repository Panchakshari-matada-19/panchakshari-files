
import fitz  # PyMuPDF
path = "results.pdf"
doc = fitz.open(path)

# page ->  image
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=200)
    pix.save(f"page_{i+1}.jpg")

print("Converted Successfully")


