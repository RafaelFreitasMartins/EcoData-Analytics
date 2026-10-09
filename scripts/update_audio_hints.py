import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to match the old audio hints block
pattern = r'<div class="audio-hints".*?</div>\s*</div>'

new_hints_html = """<div class="audio-hints" style="position: absolute; bottom: 30px; left: 30px; z-index: 10;">
        <div style="display: flex; flex-direction: column; gap: 8px; color: rgba(255, 255, 255, 0.9); font-family: 'Inter', sans-serif; font-size: 0.8rem; background: rgba(0,0,0,0.5); padding: 12px 18px; border-radius: 8px; backdrop-filter: blur(5px); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
            <div style="display: flex; align-items: center; gap: 8px;">
                <i class="ph-fill ph-hand-pointing" style="font-size: 1.1rem; color: #4CAF50;"></i>
                <span>Clique na tela para ativar o som</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <i class="ph-fill ph-mouse" style="font-size: 1.1rem; color: #f44336;"></i>
                <span>Scrolle para baixo para desativar o som</span>
            </div>
        </div>
    </div>"""

content = re.sub(pattern, new_hints_html, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Merged audio hints and reduced text size.")
