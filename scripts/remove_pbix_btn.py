import re

with open('powerbi.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the download button
content = re.sub(r'<a href="PROJETO[^\"]*\.pbix" class="external-link" download>.*?</a>', '', content, flags=re.DOTALL)

with open('powerbi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Removed PBIX download button from powerbi.html")
