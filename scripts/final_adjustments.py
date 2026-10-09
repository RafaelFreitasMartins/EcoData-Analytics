import re

# 1. Eventos.html - subtitle white color
with open('eventos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace color: #555; in .title-section p
content = re.sub(r'(\.title-section\s+p\s*\{[^}]*color:\s*)#[0-9a-fA-F]{3,6}', r'\g<1>#ffffff', content)

with open('eventos.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Participantes.html - Max width 1400px to allow 4 cards
with open('participantes.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('max-width: 1200px;', 'max-width: 1400px;')

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 3. Desafio.html - Update Card 2 text
with open('desafio.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_p_text_pattern = re.compile(r'<p>Abaetetuba \(R\$ 1,18 bi, a.*?mandioca\.</p>', re.DOTALL)
new_p_text = "<p>Abaetetuba (R$ 2,8 bi, açaí) e Santarém (R$ 2,09 bi, grãos) lideram e, juntos, ultrapassam R$ 4,89 bilhões em prejuízos acumulados. Abaetetuba, Paragominas, Santarém, Altamira e Cametá lideram o ranking de perda fisica em toneladas.</p>"
content = old_p_text_pattern.sub(new_p_text, content)

# Also update the highlight to match the new numbers just in case
old_highlight_pattern = re.compile(r'superam R\$ 2 bilh.es')
new_highlight = 'superam R$ 4,89 bilhões'
content = old_highlight_pattern.sub(new_highlight, content)

with open('desafio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates completed successfully.")
