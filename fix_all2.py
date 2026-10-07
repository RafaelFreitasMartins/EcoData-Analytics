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

new_menu = """        <ul class="menu">
            <li class="menu-item{tema_active}">
                <a href="tema.html">
                    <i class="ph ph-article"></i>
                    Tema
                </a>
            </li>
            <li class="menu-item{eventos_active}">
                <a href="eventos.html">
                    <i class="ph ph-waves"></i>
                    Fenômenos Climáticos
                </a>
            </li>
            <li class="menu-item{powerbi_active}">
                <a href="powerbi.html">
                    <i class="ph ph-shield-check"></i>
                    Power BI
                </a>
            </li>
            <li class="menu-item{desafio_active}">
                <a href="desafio.html">
                    <i class="ph ph-plant"></i>
                    Desafio
                </a>
            </li>
            <li class="menu-item{participantes_active}">
                <a href="participantes.html">
                    <i class="ph ph-users"></i>
                    Participantes
                </a>
            </li>
        </ul>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Replace Amazania
    content = content.replace('Amazania', 'Amazônia')
    content = content.replace('Amazania', 'Amazônia') # Check case?
    content = content.replace('amazania', 'amazônia')

    # 2. Re-order navigation
    # Detect which one is active
    tema_active = ' active' if file == 'tema.html' else ''
    eventos_active = ' active' if file == 'eventos.html' else ''
    powerbi_active = ' active' if file == 'powerbi.html' else ''
    desafio_active = ' active' if file == 'desafio.html' else ''
    participantes_active = ' active' if file == 'participantes.html' else ''

    current_menu = new_menu.format(
        tema_active=tema_active,
        eventos_active=eventos_active,
        powerbi_active=powerbi_active,
        desafio_active=desafio_active,
        participantes_active=participantes_active
    )

    # Regex to replace the menu
    content = re.sub(r'<ul class="menu">.*?</ul>', current_menu, content, flags=re.DOTALL)

    # 3. Remove Amazonia Legal
    content = re.sub(r'<div class="footer-location">\s*<i class="ph ph-map-pin"></i>.*?</div>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # 4. Tema: Impacto nas Culturas
    if file == 'tema.html':
        # We need to replace the text inside the card with title "Impacto nas Culturas"
        # Find the card block
        new_text = "O impacto das mudanças climáticas varia entre as culturas agrícolas: enquanto mandioca, milho, feijão caupi, cacau e soja sofrem quedas de produtividade com a falta de chuva e o calor exigindo planejamento e manejo adequado , o açaí é diretamente afetado tanto pelas secas e variações no nível dos rios em áreas de várzea quanto pela necessidade de irrigação rigorosa em terra firme."
        # regex to replace paragraph inside Impacto nas Culturas card
        content = re.sub(r'(<h3>.*?Impacto nas Culturas.*?</h3>\s*<p>).*?(</p>)', r'\g<1>' + new_text + r'\g<2>', content, flags=re.DOTALL)

    # 5. Participantes: Add Angelica
    if file == 'participantes.html':
        # Replace Participante 7
        content = re.sub(r'<div class="profile-card">\s*<img class="profile-img"[^>]*alt="Participante 7".*?</div>\s*</div>', angelica_html, content, flags=re.DOTALL)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
