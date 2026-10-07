import re
import os

files = ['eventos.html', 'powerbi.html', 'desafio.html', 'participantes.html']
base_dir = r'C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho'

for file in files:
    path = os.path.join(base_dir, file)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the background image
    content = re.sub(r"url\(['\"]?floresta-amazonica-rio-amazonas\.webp['\"]?\)", "url('amazon_river_hd.jpg')", content)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Background images updated.")
