import re

with open('participantes.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'(\.profile-img\s*\{[^}]*height:\s*)350px', r'\g<1>280px', content)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reduced image height to 280px.")
