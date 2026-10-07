import re

new_text = "O impacto das mudanças climáticas varia entre as culturas agrícolas: enquanto mandioca, milho, feijão caupi, cacau e soja sofrem quedas de produtividade com a falta de chuva e o calor exigindo planejamento e manejo adequado , o açaí é diretamente afetado tanto pelas secas e variações no nível dos rios em áreas de várzea quanto pela necessidade de irrigação rigorosa em terra firme."

with open('tema.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# We need to replace everything between <h2>...Impacto nas Culturas...</h2> and the next </div>
pattern = r'(<h2[^>]*>\s*Impacto nas Culturas\s*</h2>)(.*?)(</div>)'

def replace_card(m):
    return m.group(1) + f'\n                      <p>{new_text}</p>\n                  ' + m.group(3)

content = re.sub(pattern, replace_card, content, flags=re.DOTALL)

with open('tema.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated tema.html")
