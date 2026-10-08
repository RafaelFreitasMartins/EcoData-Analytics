import re

with open('pdf.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Just replace max-height: 100% with width: 100% and height: auto
content = re.sub(r'max-height:\s*100%;', 'width: 100%; max-width: 1000px; height: auto;', content)

with open('pdf.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated image max-height to width.")
