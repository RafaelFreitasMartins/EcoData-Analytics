import re

with open('tema.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for the old bulky slide
old_slide_pattern = r'<div class="swiper-slide"[^>]*>\s*<div class="dark-card" style="padding: 40px; max-width: 900px;[^"]*">.*?</div>\s*</div>'

new_slide = """<div class="swiper-slide" style="background-image: url('amazon_river_hd.jpg');">
                <div class="dark-card" style="border-top-color: #4CAF50;">
                    <i class="ph-fill ph-book-open" style="color: #4CAF50;"></i>
                    <h2>O Contexto</h2>
                    <div class="card-text">
                        <p>Começo com uma lembrança recente. Em 2023 e 2024, houve uma seca histórica devido ao Super El Nino. o Rio Negro chegou a 12,11 metros em Manaus, a menor cota em 122 anos de medição. Balsas com comida e combustível encalharam, e o quilo da farinha de mandioca passou de R$ 13 na capital amazonense.</p>
                        <p>Em junho de 2026, o INMET informou a volta do El Niño, com chance de intensidade forte na primavera. Então a pergunta mudou: não é mais se vai acontecer, é onde vai doer mais e com quanta antecedência dá para se preparar.</p>
                        <p>Por isso construímos uma análise cruzando quatro fontes oficiais, NOAA, INMET, IBGE e CPRM, entre 2014 e 2027, e responde quatro perguntas: quais culturas quebram mais, quais municípios perdem mais, a partir de que nível do rio o preço dispara e o que esperar da safra 2026-2027.</p>
                    </div>
                </div>
            </div>"""

content = re.sub(old_slide_pattern, new_slide, content, flags=re.DOTALL)

with open('tema.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated first slide in tema.html to match standard styling")
