import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Remove the footer text
    content = re.sub(r'<div class="footer-text">.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # 2. Update index.html
    if file == 'index.html':
        # Replace the logo
        content = content.replace('Logotipo Circular da Terra Verde.png', 'logo atualizado.jfif')
        content = content.replace('alt="Logotipo Circular da Terra Verde"', 'alt="Logo Atualizado"')
        
        # Adjust spacing in CSS
        # Logo margin-bottom
        content = re.sub(r'(\.logo\s*\{[^}]*)margin-bottom:\s*15px;', r'\1margin-bottom: 25px;', content)
        
        # H1 margins
        content = re.sub(r'(h1\s*\{[^}]*)margin-bottom:\s*8px;', r'\1margin-top: -10px;\n            margin-bottom: 35px;', content)
        
    # 3. Fix Larissa Maria's photo in participantes.html
    if file == 'participantes.html':
        content = content.replace('Larrisa%20Maria.png', 'Larissa%20Maria.png')
        content = content.replace('Larrisa Maria', 'Larissa Maria')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Adjustments completed.")
