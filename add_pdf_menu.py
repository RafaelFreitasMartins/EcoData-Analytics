import os
import glob

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

pdf_menu_item = """
            <li class="menu-item">
                <a href="pdf.html">
                    <i class="ph ph-file-pdf"></i>
                    PDF
                </a>
            </li>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "pdf.html" not in content and '<ul class="menu">' in content:
        # Find the closing </ul> of the menu
        # We can look for the Participantes li and insert after
        participantes_idx = content.find('<a href="participantes.html">')
        if participantes_idx != -1:
            end_li = content.find('</li>', participantes_idx) + 5
            content = content[:end_li] + pdf_menu_item + content[end_li:]
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added PDF menu to {os.path.basename(filepath)}")

# For pdf.html, set the active class correctly
with open(os.path.join(base_dir, "pdf.html"), 'r', encoding='utf-8') as f:
    pdf_content = f.read()

# Remove active from wherever it is
pdf_content = pdf_content.replace('class="menu-item active"', 'class="menu-item"')
# Add active to pdf.html
pdf_content = pdf_content.replace('<a href="pdf.html">', '</a></li><li class="menu-item active"><a href="pdf.html">')
# Wait, replacing like that is messy. Let's just do a smarter replace.
pdf_content = pdf_content.replace('<li class="menu-item">\n                <a href="pdf.html">', '<li class="menu-item active">\n                <a href="pdf.html">')
# Cleanup the messy replace if it happened
pdf_content = pdf_content.replace('</a></li><li class="menu-item active"><a href="pdf.html">', '<a href="pdf.html">')

with open(os.path.join(base_dir, "pdf.html"), 'w', encoding='utf-8') as f:
    f.write(pdf_content)

print("Updated active states.")
