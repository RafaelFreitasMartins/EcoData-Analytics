import re

with open('pdf.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="menu-item active"', 'class="menu-item"')
content = re.sub(r'<li class="menu-item">\s*<a href="pdf\.html">', '<li class="menu-item active">\n                <a href="pdf.html">', content)

with open('pdf.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed active class in pdf.html")
