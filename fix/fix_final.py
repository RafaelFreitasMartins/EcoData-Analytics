import re

files = ['eventos.html', 'desafio.html', 'powerbi.html', 'participantes.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Issue 1: Ensure body { flex-direction: column; } is present and there's no dangling padding block
    # Remove dangling block
    content = re.sub(r'padding:\s*40px;\s*max-width:\s*1200px;\s*margin:\s*0\s+auto;\s*width:\s*100%;\s*}', '', content)
    
    # Ensure flex-direction: column is there
    if 'flex-direction: column;' not in content:
        content = content.replace('</style>', '        body { flex-direction: column; }\n    </style>')

    # Fix Issue 2: Remove blur and opacity from body::before
    content = re.sub(r'filter:\s*blur\([^)]+\);', '', content)
    content = re.sub(r'opacity:\s*0\.6;', 'opacity: 1;', content) # or just remove opacity

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixed layout and background blur on all files.")
