import re

# 1. Update tema.html to remove autoplay
with open('tema.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace autoplay block with nothing
# We can just match the autoplay object
content = re.sub(r'autoplay:\s*\{[^}]+\},?', '', content)

with open('tema.html', 'w', encoding='utf-8') as f:
    f.write(content)


# 2. Update participantes.html to guarantee 4 cards fit
with open('participantes.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Change gap from 30px to 20px
content = re.sub(r'(\.cards-row\s*\{[^}]*gap:\s*)30px', r'\g<1>20px', content)
# Change width from 300px to 280px
content = re.sub(r'(\.profile-card\s*\{[^}]*width:\s*)300px', r'\g<1>270px', content)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated tema.html (removed autoplay) and participantes.html (adjusted card width/gap).")
