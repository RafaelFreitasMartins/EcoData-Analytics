import re

with open('participantes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the cards slightly smaller to ensure they fit 4 on almost any laptop screen
content = re.sub(r'(\.profile-card\s*\{[^}]*width:\s*)270px', r'\g<1>245px', content)
content = re.sub(r'(\.cards-row\s*\{[^}]*gap:\s*)20px', r'\g<1>15px', content)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reduced cards to 245px and gap to 15px.")
