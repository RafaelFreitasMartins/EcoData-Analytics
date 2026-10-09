import os
import glob
import re
import shutil

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

# Create directories
dirs_to_create = ['assets', 'assets/img', 'assets/media', 'assets/docs']
for d in dirs_to_create:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# Define file mappings (old_name -> new_path)
mappings = {
    'amazon_river_hd.jpg': 'assets/img/amazon_river_hd.jpg',
    'floresta-amazonica-rio-amazonas.webp': 'assets/img/floresta-amazonica-rio-amazonas.webp',
    'Emblema Verde de Terra e Folha.png': 'assets/img/Emblema Verde de Terra e Folha.png',
    'Logo novo.png': 'assets/img/Logo novo.png',
    'Logo novo_transparent.png': 'assets/img/Logo novo_transparent.png',
    'Logotipo Circular da Terra Verde.png': 'assets/img/Logotipo Circular da Terra Verde.png',
    'questionario.png': 'assets/img/questionario.png',
    'som_fundo.mp4': 'assets/media/som_fundo.mp4',
    'PROJETO (3).pbix': 'assets/docs/PROJETO (3).pbix'
}

# Move files
for old_name, new_path in mappings.items():
    old_full = os.path.join(base_dir, old_name)
    new_full = os.path.join(base_dir, new_path)
    if os.path.exists(old_full):
        shutil.move(old_full, new_full)

# Update HTML references
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace references. 
    # Use exact string replacement or regex
    for old_name, new_path in mappings.items():
        # HTML attributes like src="...", href="..."
        # and CSS like url('...')
        # We replace the literal string old_name with new_path, ensuring we only replace exact filenames
        # to avoid replacing 'assets/img/old_name' into 'assets/img/assets/img/old_name' if ran twice.
        
        # We can just replace the filename if it's preceded by a quote or slash
        # e.g., url('amazon_river_hd.jpg') -> url('assets/img/amazon_river_hd.jpg')
        # src="Logo novo_transparent.png" -> src="assets/img/Logo novo_transparent.png"
        
        # Simple replace for the known files is generally safe since their names are unique
        if old_name in content and new_path not in content:
            content = content.replace(old_name, new_path)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Assets organized and HTML files updated.")
