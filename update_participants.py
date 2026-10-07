import re

try:
    with open('participantes.html', 'r', encoding='utf-8') as f:
        html = f.read()
except UnicodeDecodeError:
    with open('participantes.html', 'r', encoding='iso-8859-1') as f:
        html = f.read()

new_grid = '''<div class="cards-grid">
                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Larrisa%20Maria.png" alt="Larissa Maria Cardoso" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>LARISSA MARIA CARDOSO</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/larissa-maria-cardoso" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/Larissa-gif-has" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:Lariiisssa.Maariaa@live.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>

                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Ivone.jpg" alt="Ivone Durães Silveira" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>IVONE DURÃES SILVEIRA</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/ivone-duraes-silveira" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/Ivoneduraes" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:iduraes99@gmail.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>

                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Derline.jpg" alt="Derline Dimanche Bertrand" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>DERLINE DIMANCHE BERTRAND</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/derlinebertrand" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/derlinedata" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:derlined@gmail.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>

                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Rafael.jpg" alt="Rafael de Freitas Martins" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>RAFAEL DE FREITAS MARTINS</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/rafaelfreitasmartins/" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/RafaelFreitasMartins" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:rafaelfreitas99@outlook.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>

                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Jhenifer.jpg" alt="Jhenifer Leticia dos Santos Martins" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>JHENIFER LETICIA DOS SANTOS MARTINS</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/jhenifer-let%C3%ADcia-dos-santos-martins-64a41b357" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/jltixx" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:jltixxmartins@gmail.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>

                <div class="profile-card">
                    <img class="profile-img" src="Imagens%20participantes/Larissa%20Natalie.jpg" alt="Larissa Natalie Caetano" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>LARISSA NATALIE CAETANO</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="https://www.linkedin.com/in/larissanatalie/" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="https://github.com/larissa-natalie" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="mailto:larissanatalieb@gmail.com" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>

                <div class="profile-card">
                    <img class="profile-img" src="https://via.placeholder.com/400x600/222222/555555?text=Foto+7" alt="Participante 7" onerror="this.src='https://via.placeholder.com/400x600/222222/555555?text=Foto'">
                    <div class="profile-gradient"></div>
                    <div class="profile-content">
                        <h3>PARTICIPANTE 7</h3>
                        <p>Desenvolvedor / Analista de Dados</p>
                        <div class="profile-socials">
                            <a href="#" target="_blank" title="LinkedIn"><i class="ph-fill ph-linkedin-logo"></i></a>
                            <a href="#" target="_blank" title="GitHub"><i class="ph-fill ph-github-logo"></i></a>
                            <a href="#" title="E-mail"><i class="ph-fill ph-envelope-simple"></i></a>
                        </div>
                    </div>
                </div>
            </div>'''

html = re.sub(
    r'<div class="cards-grid">.*?(?=</main>)',
    new_grid + '\n        ',
    html,
    flags=re.DOTALL
)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(html)
