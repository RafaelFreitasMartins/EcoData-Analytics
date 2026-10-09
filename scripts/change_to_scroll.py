import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the dblclick event listener with wheel/scroll listener
old_dblclick = r"// Para o som ao dar um duplo clique na tela\s*document\.body\.addEventListener\('dblclick', function\(e\) \{\s*var audio = document\.getElementById\('bg-audio'\);\s*if \(!audio\.paused\) \{\s*audio\.pause\(\);\s*\}\s*\}\);"

new_scroll = """// Para o som ao usar o scroll do mouse ou rolar a tela
        function stopAudioOnScroll() {
            var audio = document.getElementById('bg-audio');
            if (!audio.paused) {
                audio.pause();
            }
        }
        window.addEventListener('wheel', stopAudioOnScroll, { passive: true });
        window.addEventListener('scroll', stopAudioOnScroll, { passive: true });
        window.addEventListener('touchmove', stopAudioOnScroll, { passive: true });"""

content = re.sub(old_dblclick, new_scroll, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Changed pause trigger to scroll.")
