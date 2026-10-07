import re
import os

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"
tema_path = os.path.join(base_dir, "tema.html")
pdf_path = os.path.join(base_dir, "pdf.html")

with open(tema_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = content.replace("<title>Tema - Agroclima</title>", "<title>PDF - Agroclima</title>")

# Build the new swiper slides
slides_html = ""
for i in range(1, 5):
    img_src = f"PDF/images/pagina_{i}.jpg"
    slides_html += f"""
            <div class="swiper-slide" style="background-image: url('amazon_river_hd.jpg');">
                <div class="dark-card" style="padding: 20px; max-width: 800px; display: flex; align-items: center; justify-content: center; height: 90vh;">
                    <img src="{img_src}" alt="Página {i}" style="max-height: 100%; max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);">
                </div>
            </div>
"""

# Replace the swiper-wrapper content
# Find the start of swiper-wrapper and end of it
start_idx = content.find('<div class="swiper-wrapper">')
if start_idx != -1:
    end_idx = content.find('</div>\n        <!-- Add Pagination -->', start_idx)
    if end_idx == -1:
         end_idx = content.find('<div class="swiper-pagination">', start_idx) - 8
    
    # Slice and reconstruct
    content = content[:start_idx + len('<div class="swiper-wrapper">\n')] + slides_html + content[end_idx:]

with open(pdf_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("pdf.html created.")
