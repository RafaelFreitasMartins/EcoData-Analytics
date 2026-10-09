import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# New CSS for Header Navigation
header_css = """
        /* HEADER NAVIGATION */
        .top-header {
            background-color: #ffffff;
            border-bottom: 1px solid #f0f0f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 40px;
            height: 80px;
            position: sticky;
            top: 0;
            z-index: 1000;
            font-family: 'Inter', sans-serif;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .logo-container {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .logo-text {
            font-size: 19px;
            line-height: 1.1;
            color: #04252a; 
            letter-spacing: -0.5px;
        }

        .logo-text strong {
            font-weight: 800;
            display: block;
        }

        .logo-text span {
            font-weight: 500;
            color: #36484e;
        }

        .menu {
            list-style: none;
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 0;
            padding: 0;
        }

        .menu-item a {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 10px 16px;
            text-decoration: none;
            color: #555555;
            font-size: 14px;
            font-weight: 500;
            border-radius: 8px;
            transition: all 0.2s ease;
        }

        .menu-item a i {
            font-size: 18px;
        }

        .menu-item:hover a {
            background-color: #f5f8f5;
            color: #2e7d32;
        }

        .menu-item.active a {
            background-color: #e8f5e9;
            color: #1b5e20;
            font-weight: 600;
        }

        .main-content {
            flex: 1;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }

        body {
            flex-direction: column;
        }
"""

for file in html_files:
    if file == 'index.html':
        continue # index.html doesn't have the sidebar navigation directly like others
        
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Replace the sidebar CSS with the header CSS
    # We will just remove the old sidebar CSS and insert the new one
    content = re.sub(r'/\* ESTILOS DO MENU LATERAL \*/.*?(?=\.main-content|</style>)', header_css, content, flags=re.DOTALL)
    
    # Ensure body is flex-column if it was flex-row
    if '.main-content' not in content:
        # Just in case, add main-content basic styles
        content = content.replace('</style>', '        .main-content {\n            flex: 1;\n            padding: 40px;\n            max-width: 1200px;\n            margin: 0 auto;\n            width: 100%;\n        }\n    </style>')

    # Now replace the <aside class="sidebar"> with <header class="top-header">
    # Wait, it might be <div class="sidebar"> in some files, or <aside class="sidebar">
    sidebar_match = re.search(r'<(aside|div) class="sidebar">(.*?)</\1>', content, re.DOTALL)
    
    if sidebar_match:
        # Reconstruct the header HTML
        # Extract the menu block
        menu_match = re.search(r'<ul class="menu">(.*?)</ul>', sidebar_match.group(2), re.DOTALL)
        if menu_match:
            menu_html = f'<ul class="menu">{menu_match.group(1)}</ul>'
        else:
            menu_html = ''
            
        header_html = f"""
    <header class="top-header">
        <div class="logo-container">
            <div class="logo-text">
                <strong>EcoData</strong>
                <span>Analytics</span>
            </div>
        </div>
        {menu_html}
    </header>
"""
        # Replace the entire sidebar with the new header
        content = content[:sidebar_match.start()] + header_html + content[sidebar_match.end():]

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Navigation updated to header in all files.")
