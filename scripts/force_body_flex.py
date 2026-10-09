import re

files = ['eventos.html', 'desafio.html', 'powerbi.html', 'participantes.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure body { flex-direction: column !important; } is at the end of the style block
    if 'body { flex-direction: column' not in content:
        content = content.replace('</style>', '        body { flex-direction: column !important; }\n    </style>')

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Forced flex-direction: column on body in all files.")
