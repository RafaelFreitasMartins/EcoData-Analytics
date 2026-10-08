import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

audio_html = """
    <audio id="bg-audio" src="som_fundo.mp4" autoplay loop></audio>
    <script>
        // Força a reprodução no primeiro clique na tela caso o autoplay seja bloqueado pelo navegador
        document.body.addEventListener('click', function() {
            var audio = document.getElementById('bg-audio');
            if (audio.paused) {
                audio.play().catch(e => console.log("Audio play failed:", e));
            }
        });

        // Desliga o som imediatamente ao clicar no botão TEMA
        var temaBtn = document.querySelector('a.btn[href="tema.html"]');
        if (temaBtn) {
            temaBtn.addEventListener('click', function() {
                document.getElementById('bg-audio').pause();
            });
        }
    </script>
</body>"""

if 'id="bg-audio"' not in content:
    content = content.replace('</body>', audio_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Audio added to index.html")
