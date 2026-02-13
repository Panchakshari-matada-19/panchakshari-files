📄 PDF Utility Scripts using PyMuPDF

This project contains simple Python scripts using PyMuPDF (fitz) to:

Convert PDF pages into images

Count total number of pages in a PDF

Requirements

Python 3.x

PyMuPDF

Install dependency:

pip install pymupdf

 Script 1: Convert PDF to Images
 Description

Converts each page of a PDF file into high-quality JPG images.

How It Works

fitz.open() → Opens the PDF file

get_pixmap(dpi=200) → Converts page to image (higher DPI = better quality)

pix.save() → Saves image as JPG


-----------------------------------------------------------------------------

Script 2: Count Total Pages in PDF
Description

Displays total number of pages in a PDF file.

How It Works

doc.page_count → Returns total number of pages in the PDF

🔎 Why Use Raw String (r"")?

When using Windows paths:

r"E:\Python-tutorials\Files\results.pdf"


The r prevents escape sequence issues like:

\n

\t

Concepts Used

File handling

Third-party libraries

PDF processing

Looping and enumeration
