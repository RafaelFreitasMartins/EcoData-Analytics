import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

angelica_html = """                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Angelica.jpg" alt="Angélica da Silva" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>ANGÉLICA DA SILVA</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/ang%C3%A9lica-da-silva-6694881b5/" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/angelgomes06-ops" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:angelica.gomees06@gmail.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>"""

new_text = "O impacto das mudanças climáticas varia entre as culturas agrícolas: enquanto mandioca, milho, feijão caupi, cacau e soja sofrem quedas de produtividade com a falta de chuva e o calor exigindo planejamento e manejo adequado , o açaí é diretamente afetado tanto pelas secas e variações no nível dos rios em áreas de várzea quanto pela necessidade de irrigação rigorosa em terra firme."

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Fix mojibake for Angelica
    content = re.sub(r'<h3>ANG[^<]+LICA DA SILVA</h3>', '<h3>ANGÉLICA DA SILVA</h3>', content)
    content = content.replace('AngǸlica da Silva', 'Angélica da Silva')

    # Replace Amazania
    content = content.replace('Amazania', 'Amazônia')
    content = content.replace('amazania', 'amazônia')

    # Fix Tema text
    if file == 'tema.html':
        pattern = r'(<h2[^>]*>\s*Impacto nas Culturas\s*</h2>)(.*?)(</div>)'
        
        def replace_card(m):
            return m.group(1) + f'\n                      <p>{new_text}</p>\n                  ' + m.group(3)
        
        content = re.sub(pattern, replace_card, content, flags=re.DOTALL)
        
    # Replace the Angelica placeholder if it still exists
    if file == 'participantes.html' and 'Participante 7' in content:
        content = re.sub(r'<div class="profile-card">\s*<img class="profile-img"[^>]*alt="Participante 7".*?</div>\s*</div>', angelica_html, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixes applied successfully.")
