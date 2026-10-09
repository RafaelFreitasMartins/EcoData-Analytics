import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add the dblclick event listener
dblclick_js = """
        // Para o som ao dar um duplo clique na tela
        document.body.addEventListener('dblclick', function(e) {
            var audio = document.getElementById('bg-audio');
            if (!audio.paused) {
                audio.pause();
            }
        });
"""

# Insert right before the </script> tag closing the audio scripts
content = content.replace('</script>\n</body>', dblclick_js + '    </script>\n</body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Double click listener added.")
