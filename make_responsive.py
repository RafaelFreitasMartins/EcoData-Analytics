import glob
import os
import re

base_dir = r"C:\Users\rafae\OneDrive\Antigavity_Curriculo\Trabalho"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

responsive_css = """
        /* Responsividade Global para Celulares e Tablets */
        @media (max-width: 768px) {
            .top-header {
                flex-direction: column;
                height: auto !important;
                padding: 15px 10px 5px 10px !important;
                position: relative !important;
            }
            .logo-container {
                margin-bottom: 10px;
                justify-content: center;
                width: 100%;
            }
            .menu {
                width: 100%;
                overflow-x: auto;
                justify-content: flex-start !important;
                padding-bottom: 10px;
            }
            .menu-item a {
                white-space: nowrap;
                padding: 8px 12px !important;
                font-size: 13px !important;
            }
            .page-content {
                padding: 20px 15px !important;
            }
            
            /* Ajustes Tema e PDF */
            .dark-card {
                padding: 20px !important;
                width: 95% !important;
                max-height: 85vh !important;
                overflow-y: auto;
            }
            .dark-card h2 {
                font-size: 1.3rem !important;
            }
            .dark-card i {
                font-size: 40px !important;
                margin-bottom: 10px !important;
            }

            /* Ajustes Desafio */
            .cards-grid {
                grid-template-columns: 1fr !important;
                gap: 20px !important;
            }
            .flip-card {
                height: 480px !important;
            }
            .flip-card-front, .flip-card-back {
                padding: 20px !important;
            }
            .question {
                font-size: 1rem !important;
            }

            /* Ajustes Eventos / Fenômenos */
            .phenomenon-grid {
                grid-template-columns: 1fr !important;
            }
            .title-section h1 {
                font-size: 1.6rem !important;
            }
            .card {
                padding: 20px !important;
            }
            .card h2 {
                font-size: 1.4rem !important;
            }
            
            /* Ajustes Participantes */
            .cards-row {
                gap: 15px !important;
            }
            .profile-card {
                width: 100% !important;
                max-width: 320px;
            }
            .profile-img {
                height: 300px !important;
            }
            
            /* Ajustes Power BI */
            .iframe-container {
                min-height: 400px !important;
            }
        }
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply general responsive CSS right before closing </style>
    if responsive_css.strip() not in content and "</style>" in content:
        # Find the LAST </style> tag in the document
        last_style_index = content.rfind("</style>")
        if last_style_index != -1:
            content = content[:last_style_index] + responsive_css + content[last_style_index:]

    # Specific fix for desafio.html minmax 400px grid
    if "desafio.html" in filepath:
        content = content.replace("minmax(400px, 1fr)", "minmax(280px, 1fr)")

    # Specific fix for index.html background image if requested implicitly
    if "index.html" in filepath:
        content = re.sub(r"url\(['\"]?floresta-amazonica-rio-amazonas\.webp['\"]?\)", "url('amazon_river_hd.jpg')", content)
        content = re.sub(r'filter:\s*blur\([^)]+\);', '', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Responsive CSS applied successfully to all pages.")
