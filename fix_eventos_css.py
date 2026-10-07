import re

with open('eventos.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old sidebar CSS block completely (up to .page-content or </style>)
# The old block starts with /* ESTILOS DO MENU LATERAL
content = re.sub(r'/\* ESTILOS DO MENU LATERAL[^*]*\*/.*?(?=\.page-content|</style>)', '', content, flags=re.DOTALL)

# Now inject the correct header CSS
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

"""

# Insert the header CSS right before .page-content or </style>
if '.page-content {' in content:
    content = content.replace('.page-content {', header_css + '\n        .page-content {')
else:
    content = content.replace('</style>', header_css + '\n    </style>')

with open('eventos.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed eventos.html CSS!")
