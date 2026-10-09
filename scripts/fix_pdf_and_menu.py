import re
import os
import glob

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"

# 1. Fix pdf.html arrows
pdf_path = os.path.join(base_dir, "pdf.html")
with open(pdf_path, 'r', encoding='utf-8') as f:
    pdf_content = f.read()

if '<div class="swiper-button-next"></div>' not in pdf_content:
    pdf_content = pdf_content.replace('<div class="swiper-pagination"></div>', 
        '<div class="swiper-button-next"></div>\n            <div class="swiper-button-prev"></div>\n            <div class="swiper-pagination"></div>')

with open(pdf_path, 'w', encoding='utf-8') as f:
    f.write(pdf_content)


# 2. Reorder menu across all HTML files
html_files = glob.glob(os.path.join(base_dir, "*.html"))

menu_items_order = ["tema", "eventos", "powerbi", "pdf", "desafio", "participantes"]

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    start_idx = content.find('<ul class="menu">')
    if start_idx == -1:
        continue
    
    end_idx = content.find('</ul>', start_idx)
    menu_content = content[start_idx:end_idx]
    
    # Extract all <li> blocks
    # We can use a regex that matches <li class="menu-item..."> ... </li>
    li_pattern = re.compile(r'<li class="menu-item[^>]*>.*?</li>', re.DOTALL)
    items = li_pattern.findall(menu_content)
    
    if not items:
        continue
        
    # Sort them according to menu_items_order
    def get_order(item):
        for i, name in enumerate(menu_items_order):
            if f'href="{name}.html"' in item:
                return i
        return 99
        
    items.sort(key=get_order)
    
    # Rebuild menu
    new_menu_content = '<ul class="menu">\n            ' + '\n            '.join(items) + '\n        '
    
    # Replace in content
    content = content[:start_idx] + new_menu_content + content[end_idx:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
print("Arrows added to pdf.html and menus reordered successfully.")
