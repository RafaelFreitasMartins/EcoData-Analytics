import re

# Update text in desafio.html
with open('desafio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The text to replace
old_text = r"Abaixo de 15 m no Porto de Manaus. Nesse ponto o spread da farinha Manaus.*?rotas a.reas e estoques reguladores."
new_text = r"Abaixo de 15 m no Porto de Manaus. Nesse ponto o spread da farinha Manaus × Belém passa de ~8% para mais de 45%, e a farinha salta de R$ 7,55 para até R$ 13,28/kg. Entre 15 e 18 m é zona de atenção; abaixo de 15 m é preciso acionar rotas aéreas e estoques reguladores."

content = re.sub(old_text, new_text, content, flags=re.DOTALL)

# Update the highlight too
old_highlight = r"R\$ 13,30/kg"
new_highlight = r"R$ 13,28/kg"
content = re.sub(old_highlight, new_highlight, content)

with open('desafio.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update index.html background image opacity
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace('opacity: 0.8;', 'opacity: 1;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updates applied to desafio.html and index.html")
