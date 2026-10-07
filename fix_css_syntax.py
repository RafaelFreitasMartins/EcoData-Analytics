import re
import os

files = ['desafio.html', 'participantes.html', 'powerbi.html', 'eventos.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to replace this exact broken block:
    broken_block = """
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }

        body {
            flex-direction: column;
        }
"""
    
    fixed_block = """
        body {
            flex-direction: column;
        }
"""
    
    if broken_block in content:
        content = content.replace(broken_block, fixed_block)
        print(f"Fixed syntax error in {file}")
    else:
        # Maybe slightly different whitespace? Let's use regex
        # Look for the hanging padding: 40px; ... } body { flex-direction: column; }
        pattern = re.compile(r'padding:\s*40px;\s*max-width:\s*1200px;\s*margin:\s*0\s+auto;\s*width:\s*100%;\s*}\s*body\s*{\s*flex-direction:\s*column;\s*}')
        content = pattern.sub('body { flex-direction: column; }', content)
        print(f"Regex fixed syntax error in {file}")
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("All files fixed.")
