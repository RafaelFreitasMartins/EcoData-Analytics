import re

with open('powerbi.html', 'r', encoding='utf-8') as f:
    content = f.read()

btn_html = """    <main>
        <div style="margin-bottom: 20px;">
            <a href="tema.html" style="display: inline-flex; align-items: center; gap: 8px; background-color: #2e7d32; color: #fff; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 600; font-family: 'Inter', sans-serif; transition: background-color 0.2s; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <i class="ph ph-arrow-left" style="font-size: 20px;"></i>
                Voltar para o Tema
            </a>
        </div>"""

content = content.replace('<main>', btn_html)

# Add hover effect in CSS if not present
hover_css = """
        .back-btn:hover {
            background-color: #1b5e20 !important;
        }
"""
content = content.replace('style="display: inline-flex;', 'class="back-btn" style="display: inline-flex;')
if '.back-btn:hover' not in content:
    content = content.replace('</style>', hover_css + '\n    </style>')

with open('powerbi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added Back button to powerbi.html")
