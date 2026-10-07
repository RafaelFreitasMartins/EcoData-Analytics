import re

with open('participantes.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix font size
html = re.sub(r'font-size: 1.8rem;', 'font-size: 1.3rem;', html)

# Fix Ivone's name
html = re.sub(r'IVONE DUR.*?ES SILVEIRA', 'IVONE DURÃES SILVEIRA', html)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(html)
