import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert volume setting at the beginning of the script block
volume_js = """
        // Define o volume inicial do som ambiente (0.0 a 1.0)
        document.getElementById('bg-audio').volume = 0.3;
"""

if "volume = 0.3" not in content:
    content = content.replace("<script>\n        // Força a reprodução", "<script>\n" + volume_js + "\n        // Força a reprodução")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Volume set to 30%.")
