import fitz
import os

pdf_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho\PDF"
image_dir = os.path.join(pdf_dir, "images")

if not os.path.exists(image_dir):
    os.makedirs(image_dir)

files = ["Pagina 1.pdf", "Pagina 2.pdf", "Pagina 3.pdf", "Pagina 4.pdf"]

for i, filename in enumerate(files, 1):
    path = os.path.join(pdf_dir, filename)
    if os.path.exists(path):
        doc = fitz.open(path)
        page = doc.load_page(0)  # first page
        pix = page.get_pixmap(dpi=150)
        out_path = os.path.join(image_dir, f"pagina_{i}.jpg")
        pix.save(out_path)
        print(f"Saved {out_path}")
    else:
        print(f"File not found: {path}")

