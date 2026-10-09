import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

hints_html = """    <div class="audio-hints" style="position: absolute; bottom: 30px; left: 30px; display: flex; flex-direction: column; gap: 10px; z-index: 10; animation: fadeIn 2s ease-in-out;">
        <div style="display: flex; align-items: center; gap: 10px; color: rgba(255, 255, 255, 0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; background: rgba(0,0,0,0.5); padding: 10px 15px; border-radius: 8px; backdrop-filter: blur(5px); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
            <i class="ph-fill ph-hand-pointing" style="font-size: 1.4rem;"></i>
            <span>Clique na tela para ativar o som</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; color: rgba(255, 255, 255, 0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; background: rgba(0,0,0,0.5); padding: 10px 15px; border-radius: 8px; backdrop-filter: blur(5px); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
            <i class="ph-fill ph-arrows-down-up" style="font-size: 1.4rem;"></i>
            <span>Scrolle para baixo para desativar o som</span>
        </div>
    </div>
"""

# Let's use ph-mouse if they prefer mouse icon, actually I'll use a combination:
hints_html = """    <div class="audio-hints" style="position: absolute; bottom: 30px; left: 30px; display: flex; flex-direction: column; gap: 10px; z-index: 10;">
        <div style="display: flex; align-items: center; gap: 10px; color: rgba(255, 255, 255, 0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; background: rgba(0,0,0,0.5); padding: 10px 15px; border-radius: 8px; backdrop-filter: blur(5px); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
            <i class="ph-fill ph-hand-pointing" style="font-size: 1.4rem; color: #4CAF50;"></i>
            <span>Clique na tela para ativar o som</span>
        </div>
        <div style="display: flex; align-items: center; gap: 10px; color: rgba(255, 255, 255, 0.9); font-family: 'Inter', sans-serif; font-size: 0.95rem; background: rgba(0,0,0,0.5); padding: 10px 15px; border-radius: 8px; backdrop-filter: blur(5px); box-shadow: 0 4px 6px rgba(0,0,0,0.2);">
            <i class="ph-fill ph-mouse" style="font-size: 1.4rem; color: #f44336;"></i>
            <span>Scrolle para baixo para desativar o som</span>
        </div>
    </div>
"""

if "audio-hints" not in content:
    content = content.replace('</body>', hints_html + '\n</body>')

# Responsive tweak just in case screen is small
css_tweak = """
    <style>
        @media (max-width: 768px) {
            .audio-hints {
                bottom: 15px !important;
                left: 15px !important;
                gap: 5px !important;
            }
            .audio-hints div {
                font-size: 0.8rem !important;
                padding: 6px 10px !important;
            }
            .audio-hints i {
                font-size: 1.1rem !important;
            }
        }
    </style>
"""
if "audio-hints" not in content: # This logic is fine because it was already replaced above.
    pass

content = content.replace('</head>', css_tweak + '\n</head>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added audio hints to index.html")
