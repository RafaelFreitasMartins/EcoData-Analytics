import re

with open('participantes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert to original dimensions
content = re.sub(r'(\.profile-card\s*\{[^}]*width:\s*)245px', r'\g<1>300px', content)
content = re.sub(r'(\.cards-row\s*\{[^}]*gap:\s*)15px', r'\g<1>30px', content)
content = re.sub(r'(\.profile-img\s*\{[^}]*height:\s*)280px', r'\g<1>350px', content)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored original card dimensions.")
