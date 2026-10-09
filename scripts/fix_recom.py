import re

with open('recomendacoes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <main> and its contents
main_pattern = r'<main>.*?</main>'

recom_main = """<main class="page-content" style="align-items: center; justify-content: center; height: 100%; display: flex; flex-direction: column;">
        <div class="header-title" style="text-align: center; margin-bottom: 30px;">
            <h1 style="color: #ffffff; font-size: 2.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5); margin: 0;">Recomendações Estratégicas</h1>
        </div>
        
        <div class="recom-grid" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; width: 100%; max-width: 1300px; margin-top: 20px;">
            
            <div class="recom-card" style="background: rgba(255, 255, 255, 0.95); padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #fbc02d; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <i class="ph-fill ph-warning-circle" style="font-size: 55px; color: #fbc02d; margin-bottom: 20px;"></i>
                <p style="font-size: 1.15rem; line-height: 1.6; color: #333; margin: 0;">Monitorar o ONI e usar o alerta em três cores. Amarelo, entre 15 e 18 metros, é o sinal para formar estoques. Vermelho, abaixo de 15, é o gatilho para rotas aéreas e distribuição emergencial.</p>
            </div>
            
            <div class="recom-card" style="background: rgba(255, 255, 255, 0.95); padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #1976d2; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <i class="ph-fill ph-handshake" style="font-size: 55px; color: #1976d2; margin-bottom: 20px;"></i>
                <p style="font-size: 1.15rem; line-height: 1.6; color: #333; margin: 0;">Priorizar apoio, como crédito, seguro e assistência técnica, nos municípios de maior prejuízo, começando por Abaetetuba e Santarém.</p>
            </div>
            
            <div class="recom-card" style="background: rgba(255, 255, 255, 0.95); padding: 40px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.2); border-top: 6px solid #388e3c; display: flex; flex-direction: column; align-items: center; text-align: center;">
                <i class="ph-fill ph-plant" style="font-size: 55px; color: #388e3c; margin-bottom: 20px;"></i>
                <p style="font-size: 1.15rem; line-height: 1.6; color: #333; margin: 0;">Proteger a mandioca, por ser a base alimentar, e diversificar a renda do açaí.</p>
            </div>
            
        </div>
    </main>"""

content = re.sub(main_pattern, recom_main, content, flags=re.DOTALL)

with open('recomendacoes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed recomendacoes.html main content")
