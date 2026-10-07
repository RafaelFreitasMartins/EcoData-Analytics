import re

try:
    with open('participantes.html', 'r', encoding='utf-8') as f:
        html = f.read()
except UnicodeDecodeError:
    with open('participantes.html', 'r', encoding='iso-8859-1') as f:
        html = f.read()

replacement = '''<img class="profile-img" src="Imagens%20participantes/Larrisa%20Maria.png" alt="Larissa Maria Cardoso">
                    
                    <div class="profile-gradient"></div>
                    
                    <div class="profile-content">
                        <h3>LARISSA MARIA CARDOSO</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/larissa-maria-cardoso" target="_blank" title="LinkedIn">
                                <i class="ph-fill ph-linkedin-logo"></i>
                            </a>
                            <a href="https://github.com/Larissa-gif-has" target="_blank" title="GitHub">
                                <i class="ph-fill ph-github-logo"></i>
                            </a>
                            <a href="mailto:Lariiisssa.Maariaa@live.com" title="E-mail">
                                <i class="ph-fill ph-envelope-simple"></i>
                            </a>'''

html = re.sub(
    r'<img class="profile-img" src="https://via.placeholder.com/400x600/222222/555555\?text=Foto\+1".*?<a href="mailto:contato1@email.com" title="E-mail">\s*<i class="ph-fill ph-envelope-simple"></i>\s*</a>',
    replacement,
    html,
    flags=re.DOTALL
)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(html)
