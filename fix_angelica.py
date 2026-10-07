import re
with open('participantes.html', 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

c = re.sub(r'<h3>ANG.*? DA SILVA</h3>', '<h3>ANGÉLICA DA SILVA</h3>', c)
c = re.sub(r'alt="Ang.*? da Silva"', 'alt="Angélica da Silva"', c)
c = c.replace('ANG%LICA', 'ANGÉLICA')

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(c)
