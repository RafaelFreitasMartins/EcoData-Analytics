import re

with open('desafio.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Force 2 columns on desktop
content = re.sub(
    r'\.cards-grid\s*\{[^}]*grid-template-columns:[^;]+;', 
    r'.cards-grid {\n            display: grid;\n            grid-template-columns: 1fr 1fr;\n            gap: 30px;\n            justify-content: center;', 
    content
)

# If the regex didn't catch properly because of my earlier replacement, let's do a more robust one
if 'grid-template-columns: repeat(' in content or 'grid-template-columns: minmax(' in content or 'grid-template-columns: 1fr 1fr;' not in content:
    # Just replace the whole block if needed, but let's see if we can target it.
    content = re.sub(r'grid-template-columns:\s*repeat\([^)]+\);', 'grid-template-columns: 1fr 1fr;', content)
    content = re.sub(r'grid-template-columns:\s*minmax\([^)]+\);', 'grid-template-columns: 1fr 1fr;', content)

# 2. Increase height of flip-card on desktop
content = re.sub(r'(\.flip-card\s*\{[^}]*height:\s*)\d+px;', r'\g<1>480px;', content)

# 3. Disable scrollbar on back card
content = re.sub(r'overflow-y:\s*auto;', 'overflow-y: hidden;', content)
# Remove the custom scrollbar CSS just to clean up
content = re.sub(r'\.flip-card-back::-webkit-scrollbar.*?\}', '', content, flags=re.DOTALL)

# 4. Update responsive height for mobile so it fits the narrow wrapping text
content = re.sub(r'(\.flip-card\s*\{\s*height:\s*)480px\s*!important;', r'\g<1>550px !important;', content)

with open('desafio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated desafio.html for 2 columns and no scroll.")
