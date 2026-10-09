import re
import os
import glob

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

# ==========================================
# 1. ADD FIRST SLIDE TO TEMA.HTML
# ==========================================
tema_path = os.path.join(base_dir, "tema.html")
with open(tema_path, 'r', encoding='utf-8') as f:
    tema_content = f.read()

new_slide = """
            <div class="swiper-slide" style="background-image: url('amazon_river_hd.jpg');">
                <div class="dark-card" style="padding: 40px; max-width: 900px; display: flex; flex-direction: column; align-items: flex-start; justify-content: center; height: 85vh; text-align: left; overflow-y: auto;">
                    <h2 style="margin-bottom: 25px; text-align: center; width: 100%;"><i class="ph-fill ph-book-open"></i> O Contexto</h2>
                    <p style="font-size: 1.15rem; line-height: 1.6; margin-bottom: 15px;">Começo com uma lembrança recente. Em 2023 e 2024, houve uma seca histórica devido ao Super El Nino. o Rio Negro chegou a 12,11 metros em Manaus, a menor cota em 122 anos de medição. Balsas com comida e combustível encalharam, e o quilo da farinha de mandioca passou de R$ 13 na capital amazonense.</p>
                    <p style="font-size: 1.15rem; line-height: 1.6; margin-bottom: 15px;">Em junho de 2026, o INMET informou a volta do El Niño, com chance de intensidade forte na primavera. Então a pergunta mudou: não é mais se vai acontecer, é onde vai doer mais e com quanta antecedência dá para se preparar.</p>
                    <p style="font-size: 1.15rem; line-height: 1.6;">Por isso construímos uma análise cruzando quatro fontes oficiais, NOAA, INMET, IBGE e CPRM, entre 2014 e 2027, e responde quatro perguntas: quais culturas quebram mais, quais municípios perdem mais, a partir de que nível do rio o preço dispara e o que esperar da safra 2026-2027.</p>
                </div>
            </div>
"""

# Insert right after <div class="swiper-wrapper">
if "Começo com uma lembrança recente" not in tema_content:
    tema_content = tema_content.replace('<div class="swiper-wrapper">', '<div class="swiper-wrapper">\n' + new_slide)
    with open(tema_path, 'w', encoding='utf-8') as f:
        f.write(tema_content)
    print("Added main slide to tema.html")

# ==========================================
# 2. CREATE DADOS-ARQUITETURA.HTML
# ==========================================
with open(os.path.join(base_dir, "recomendacoes.html"), 'r', encoding='utf-8') as f:
    template = f.read()

# Replace Title
dados_content = re.sub(r'<title>.*?</title>', '<title>Dados e Arquitetura - Agroclima</title>', template)
# Fix active menu (will be replaced safely later but we clear it for now)
dados_content = dados_content.replace('class="menu-item active"', 'class="menu-item"')

# Build the main content for Dados e Arquitetura
main_pattern = r'<main.*?</main>'

dados_main = """<main class="page-content" style="align-items: center; justify-content: flex-start; min-height: 100vh; display: flex; flex-direction: column; padding: 40px 20px;">
        <div class="header-title" style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #ffffff; font-size: 2.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin: 0;">Dados e Arquitetura</h1>
        </div>
        
        <div class="cards-grid" style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 25px; width: 100%; max-width: 1200px; margin-bottom: 25px;">
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #2196f3;">
                <h3 style="margin-top: 0; display: flex; align-items: center; gap: 10px; color: #1565c0; font-size: 1.4rem;"><i class="ph-fill ph-waves"></i> NOAA</h3>
                <p style="color: #333; line-height: 1.5;"><strong>A NOAA (National Oceanic and Atmospheric Administration, ou Administração Oceânica e Atmosférica Nacional)</strong></p>
                <p style="color: #444; line-height: 1.5;"><strong>Principais funções:</strong> Previsão do tempo e meteorologia, Monitoramento oceânico e climático, Preservação ambiental e pesca.</p>
            </div>
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #4caf50;">
                <h3 style="margin-top: 0; display: flex; align-items: center; gap: 10px; color: #2e7d32; font-size: 1.4rem;"><i class="ph-fill ph-cloud-sun"></i> INMET</h3>
                <p style="color: #333; line-height: 1.5;"><strong>Órgão governamental:</strong> É uma instituição pública federal vinculada ao Ministério da Agricultura e Pecuária (MAPA).</p>
                <p style="color: #444; line-height: 1.5;"><strong>Missão principal:</strong> Monitorar o tempo e o clima, emitir previsões meteorológicas e publicar avisos de eventos climáticos severos no Brasil.</p>
            </div>
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #ff9800;">
                <h3 style="margin-top: 0; display: flex; align-items: center; gap: 10px; color: #e65100; font-size: 1.4rem;"><i class="ph-fill ph-mountains"></i> CPRM</h3>
                <p style="color: #333; line-height: 1.5;"><strong>Companhia de Pesquisa de Recursos Minerais.</strong></p>
                <p style="color: #444; line-height: 1.5;"><strong>Principais funções:</strong> Gestão de Recursos Hídricos, Prevenção de Desastres Naturais e Estudos de Geodiversidade.</p>
            </div>
            
            <div style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #9c27b0;">
                <h3 style="margin-top: 0; display: flex; align-items: center; gap: 10px; color: #6a1b9a; font-size: 1.4rem;"><i class="ph-fill ph-graph"></i> Modelo em Estrela</h3>
                <p style="color: #444; line-height: 1.5;">No centro ficam as tabelas fato e em volta as dimensões. Tabelas fato diferentes compartilhando as mesmas dimensões (Star Schema).</p>
            </div>
        </div>

        <div style="background: rgba(255, 255, 255, 0.95); padding: 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); width: 100%; max-width: 1200px; text-align: center; border-top: 6px solid #333;">
            <h3 style="margin-top: 0; color: #333; font-size: 1.5rem; margin-bottom: 25px;">Tecnologias Utilizadas</h3>
            <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 40px;">
                <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <i class="ph-fill ph-database" style="font-size: 60px; color: #0277bd;"></i>
                    <strong style="font-size: 1.1rem; color: #444;">SQL</strong>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <i class="ph-fill ph-chart-bar" style="font-size: 60px; color: #f2c811;"></i>
                    <strong style="font-size: 1.1rem; color: #444;">POWER BI</strong>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <i class="ph-fill ph-brain" style="font-size: 60px; color: #e91e63;"></i>
                    <strong style="font-size: 1.1rem; color: #444;">IA</strong>
                </div>
                <div style="display: flex; flex-direction: column; align-items: center; gap: 10px;">
                    <i class="ph-fill ph-rocket-launch" style="font-size: 60px; color: #000000;"></i>
                    <strong style="font-size: 1.1rem; color: #444;">ANTIGRAVITY</strong>
                </div>
            </div>
        </div>
    </main>"""

dados_content = re.sub(main_pattern, dados_main, dados_content, flags=re.DOTALL)

with open(os.path.join(base_dir, "dados-arquitetura.html"), 'w', encoding='utf-8') as f:
    f.write(dados_content)

print("Created dados-arquitetura.html")

# ==========================================
# 3. ADD TO MENU IN ALL FILES
# ==========================================
html_files = glob.glob(os.path.join(base_dir, "*.html"))
for filepath in html_files:
    if "index.html" in filepath or "powerbi.html" in filepath:
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'href="dados-arquitetura.html"' in content:
        continue

    menu_item = """
            <li class="menu-item">
                <a href="dados-arquitetura.html">
                    <i class="ph ph-database"></i>
                    Dados e Arquitetura
                </a>
            </li>"""

    # Insert after Tema
    # Look for </a>\s*</li> after href="tema.html"
    tema_pattern = re.compile(r'<a href="tema\.html">.*?</a>\s*</li>', re.DOTALL)
    match = tema_pattern.search(content)
    if match:
        idx = match.end()
        content = content[:idx] + menu_item + content[idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

# 4. Make it active on its own page
with open(os.path.join(base_dir, "dados-arquitetura.html"), 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<li class="menu-item">\n                <a href="dados-arquitetura.html">', 
                          '<li class="menu-item active">\n                <a href="dados-arquitetura.html">')

with open(os.path.join(base_dir, "dados-arquitetura.html"), 'w', encoding='utf-8') as f:
    f.write(content)

print("Menu updated with Dados e Arquitetura")
