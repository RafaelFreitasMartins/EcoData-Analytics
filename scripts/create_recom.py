import re
import os
import glob

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

# 1. Create recomendacoes.html based on desafio.html
with open(os.path.join(base_dir, "desafio.html"), 'r', encoding='utf-8') as f:
    desafio_content = f.read()

# Replace Title
recom_content = re.sub(r'<title>.*?</title>', '<title>Recomendações - Agroclima</title>', desafio_content)

# Replace the active menu item
recom_content = recom_content.replace('class="menu-item active"', 'class="menu-item"')

# We will add the "Recomendações" link to the menu later across ALL files, 
# so we don't need to manually inject it here just yet.

# Replace <main> content
main_pattern = r'<main class="page-content">.*?</main>'

recom_main = """<main class="page-content" style="align-items: center; justify-content: center; height: 100%;">
        <div class="header-title" style="text-align: center; margin-bottom: 20px;">
            <h1 style="color: #ffffff; font-size: 2.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin: 0;">Recomendações Estratégicas</h1>
        </div>
        
        <div class="recom-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; width: 100%; max-width: 1200px; margin-top: 20px;">
            
            <div class="recom-card" style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #4CAF50; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <i class="ph-fill ph-warning-circle" style="font-size: 45px; color: #d32f2f; margin-bottom: 20px;"></i>
                <p style="font-size: 1.15rem; line-height: 1.6; color: #333; margin: 0;">Monitorar o ONI e usar o alerta em três cores. Amarelo, entre 15 e 18 metros, é o sinal para formar estoques. Vermelho, abaixo de 15, é o gatilho para rotas aéreas e distribuição emergencial.</p>
            </div>
            
            <div class="recom-card" style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #4CAF50; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <i class="ph-fill ph-handshake" style="font-size: 45px; color: #1976d2; margin-bottom: 20px;"></i>
                <p style="font-size: 1.15rem; line-height: 1.6; color: #333; margin: 0;">Priorizar apoio, como crédito, seguro e assistência técnica, nos municípios de maior prejuízo, começando por Abaetetuba e Santarém.</p>
            </div>
            
            <div class="recom-card" style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #4CAF50; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <i class="ph-fill ph-plant" style="font-size: 45px; color: #388e3c; margin-bottom: 20px;"></i>
                <p style="font-size: 1.15rem; line-height: 1.6; color: #333; margin: 0;">Proteger a mandioca, por ser a base alimentar, e diversificar a renda do açaí.</p>
            </div>
            
        </div>
    </main>"""

recom_content = re.sub(main_pattern, recom_main, recom_content, flags=re.DOTALL)

# Add responsive CSS for recom-grid
responsive_recom = """
            /* Ajustes Recomendações */
            .recom-grid {
                grid-template-columns: 1fr !important;
                gap: 20px !important;
            }
"""
recom_content = recom_content.replace('/* Ajustes Eventos / Fenômenos */', responsive_recom + '\n            /* Ajustes Eventos / Fenômenos */')

with open(os.path.join(base_dir, "recomendacoes.html"), 'w', encoding='utf-8') as f:
    f.write(recom_content)

print("Created recomendacoes.html")


# 2. Add "Recomendações" to the menu across all files
# It should be placed BEFORE Participantes
for filepath in html_files:
    if filepath.endswith("index.html") or filepath.endswith("powerbi.html"):
        continue  # These don't use the standard top-header menu, or use a customized one (powerbi)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'href="recomendacoes.html"' in content:
        continue
    
    # We want to insert it right before the Participantes menu item
    recom_menu_html = """
            <li class="menu-item">
                <a href="recomendacoes.html">
                    <i class="ph ph-lightbulb"></i>
                    Recomendações
                </a>
            </li>"""
            
    # Find the Participantes li and insert before it
    # <li class="menu-item">\n                <a href="participantes.html">
    # Try different combinations just in case of active class
    participantes_pattern = re.compile(r'<li class="menu-item[^>]*>\s*<a href="participantes\.html">')
    match = participantes_pattern.search(content)
    if match:
        idx = match.start()
        content = content[:idx] + recom_menu_html + "\n" + content[idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Recomendações menu to {os.path.basename(filepath)}")

# 3. Add to the new recomendacoes.html as well
with open(os.path.join(base_dir, "recomendacoes.html"), 'r', encoding='utf-8') as f:
    content = f.read()

participantes_pattern = re.compile(r'<li class="menu-item[^>]*>\s*<a href="participantes\.html">')
match = participantes_pattern.search(content)
if match:
    idx = match.start()
    recom_menu_html = """
            <li class="menu-item active">
                <a href="recomendacoes.html">
                    <i class="ph ph-lightbulb"></i>
                    Recomendações
                </a>
            </li>"""
    content = content[:idx] + recom_menu_html + "\n" + content[idx:]

with open(os.path.join(base_dir, "recomendacoes.html"), 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated menu in recomendacoes.html with active state")
