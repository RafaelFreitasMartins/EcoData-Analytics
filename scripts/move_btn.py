import re

with open('powerbi.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the button from main
content = re.sub(r'<div style="margin-bottom: 20px;">\s*<a href="tema\.html".*?</a>\s*</div>', '', content, flags=re.DOTALL)

# 2. Update the header
old_header = r'<header>\s*<a href="index\.html".*?</a>\s*<a href="PROJETO \(3\)\.pbix".*?</a>\s*</header>'

new_header = """<header>
        <a href="index.html" class="back-btn">← Voltar para o Início</a>
        <div style="display: flex; gap: 15px; align-items: center;">
            <a href="tema.html" class="back-btn" style="display: inline-flex; align-items: center; gap: 8px; background-color: #2e7d32; color: #fff; padding: 8px 15px; border-radius: 6px; text-decoration: none; font-weight: 600; font-family: 'Inter', sans-serif; transition: background-color 0.2s; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <i class="ph ph-arrow-left" style="font-size: 18px;"></i>
                Voltar para o Tema
            </a>
            <a href="PROJETO (3).pbix" class="external-link" download>Baixar Arquivo PBIX ↓</a>
        </div>
    </header>"""

content = re.sub(old_header, new_header, content, flags=re.DOTALL)

with open('powerbi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Moved button to the header.")
