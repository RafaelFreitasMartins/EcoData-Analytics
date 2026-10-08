import re

with open('pdf.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="PDF/images/pagina_2.jpg"', 'src="PDF/pd_tela_segunda_tela.png"')

with open('pdf.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated image 2 in pdf.html")
