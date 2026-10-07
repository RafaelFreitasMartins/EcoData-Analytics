import re
from bs4 import BeautifulSoup

with open('tema.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all tema-cards
cards = soup.find_all('div', class_='tema-card')

themes = []
for card in cards:
    # Get color from inline style if any
    color = "#4CAF50" # default
    style = card.get('style', '')
    m = re.search(r'border-left-color:\s*(#[a-fA-F0-9]+)', style)
    if m:
        color = m.group(1)
        
    icon = card.find('i')
    icon_classes = " ".join(icon['class']) if icon else "ph-fill ph-leaf"
    
    # Title
    h2 = card.find('h2')
    # Remove icon from h2 text
    if h2.find('i'):
        h2.find('i').decompose()
    title = h2.text.strip() if h2 else "Tema"
    
    # Paragraphs
    paragraphs = [p.text for p in card.find_all('p')]
    
    themes.append({
        'color': color,
        'icon_classes': icon_classes,
        'title': title,
        'paragraphs': paragraphs
    })

# Background images mapping
bgs = [
    "amazon_river_hd.jpg",
    "https://images.unsplash.com/photo-1515694346937-94d85e41e6f0?auto=format&fit=crop&w=1920&q=80",
    "https://images.unsplash.com/photo-1508412853235-900350711718?auto=format&fit=crop&w=1920&q=80",
    "https://images.unsplash.com/photo-1500937386664-56d1dfef3854?auto=format&fit=crop&w=1920&q=80",
    "https://images.unsplash.com/photo-1542408990-2646dff21e10?auto=format&fit=crop&w=1920&q=80",
    "https://images.unsplash.com/photo-1533900298318-6b8da08a523e?auto=format&fit=crop&w=1920&q=80",
    "floresta-amazonica-rio-amazonas.webp"
]

# Generate Swiper HTML
slides_html = ""
for i, theme in enumerate(themes):
    bg = bgs[i % len(bgs)]
    color = theme['color']
    icon_cls = theme['icon_classes']
    title = theme['title']
    
    ps_html = "".join([f"<p>{p}</p>" for p in theme['paragraphs']])
    
    slides_html += f"""
        <div class="swiper-slide" style="background-image: url('{bg}');">
            <div class="dark-card" style="border-top-color: {color};">
                <i class="{icon_cls}" style="color: {color};"></i>
                <h2>{title}</h2>
                <div class="card-text">
                    {ps_html}
                </div>
            </div>
        </div>
"""

new_tema_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tema - Agroclima</title>
    <!-- Fontes e Ícones -->
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    
    <!-- Swiper CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.css" />

    <style>
        :root {{
            --primary-color: #2e7d32;
            --text-color: #333;
            --bg-color: #111;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}
        
        /* HEADER NAVIGATION */
        .top-header {{
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
        }}
        .logo-container {{ display: flex; align-items: center; gap: 12px; }}
        .logo-text {{ font-size: 19px; line-height: 1.1; color: #04252a; letter-spacing: -0.5px; }}
        .logo-text strong {{ font-weight: 800; display: block; }}
        .logo-text span {{ font-weight: 500; color: #36484e; }}
        .menu {{ list-style: none; display: flex; align-items: center; gap: 10px; margin: 0; padding: 0; }}
        .menu-item a {{
            display: flex; align-items: center; gap: 8px;
            padding: 10px 16px; text-decoration: none; color: #555555;
            font-size: 14px; font-weight: 500; border-radius: 8px; transition: all 0.2s ease;
        }}
        .menu-item a i {{ font-size: 18px; }}
        .menu-item:hover a {{ background-color: #f5f8f5; color: #2e7d32; }}
        .menu-item.active a {{ background-color: #e8f5e9; color: #1b5e20; font-weight: 600; }}

        /* MAIN AND SWIPER */
        .main-content {{
            flex: 1;
            width: 100%;
            display: flex;
        }}
        .swiper {{
            width: 100%;
            height: calc(100vh - 80px); /* Fill remaining height */
        }}
        .swiper-slide {{
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            padding: 20px;
        }}
        .swiper-slide::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.6); /* Dark overlay */
            z-index: 1;
        }}
        
        /* DESAFIO-STYLE DARK CARD */
        .dark-card {{
            position: relative;
            z-index: 2;
            background-color: #1a1a1a;
            border-radius: 12px;
            padding: 40px;
            max-width: 650px;
            width: 100%;
            color: #ffffff;
            border-top: 6px solid #4CAF50;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
            text-align: center;
            max-height: 85vh;
            display: flex;
            flex-direction: column;
        }}
        .dark-card i {{
            font-size: 54px;
            margin-bottom: 15px;
        }}
        .dark-card h2 {{
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 25px;
            color: #ffffff;
        }}
        .card-text {{
            overflow-y: auto;
            text-align: justify;
            padding-right: 10px;
        }}
        .card-text p {{
            font-size: 0.95rem;
            color: #cccccc;
            line-height: 1.6;
            margin-bottom: 15px;
        }}
        .card-text p:last-child {{
            margin-bottom: 0;
        }}
        
        /* Custom Scrollbar for card text */
        .card-text::-webkit-scrollbar {{ width: 6px; }}
        .card-text::-webkit-scrollbar-track {{ background: #2a2a2a; border-radius: 4px; }}
        .card-text::-webkit-scrollbar-thumb {{ background: #555; border-radius: 4px; }}
        
        /* Swiper Controls Customization */
        .swiper-button-next, .swiper-button-prev {{
            color: #ffffff;
            text-shadow: 0 2px 5px rgba(0,0,0,0.5);
        }}
        .swiper-pagination-bullet {{
            background: #ffffff;
            opacity: 0.5;
        }}
        .swiper-pagination-bullet-active {{
            opacity: 1;
            background: #4CAF50;
        }}
    </style>
</head>
<body>

    <header class="top-header">
        <div class="logo-container">
            <div class="logo-text">
                <strong>EcoData</strong>
                <span>Analytics</span>
            </div>
        </div>
        <ul class="menu">
            <li class="menu-item active">
                <a href="tema.html">
                    <i class="ph ph-article"></i>
                    Tema
                </a>
            </li>
            <li class="menu-item">
                <a href="eventos.html">
                    <i class="ph ph-waves"></i>
                    Fenômenos Climáticos
                </a>
            </li>
            <li class="menu-item">
                <a href="powerbi.html">
                    <i class="ph ph-shield-check"></i>
                    Power BI
                </a>
            </li>
            <li class="menu-item">
                <a href="desafio.html">
                    <i class="ph ph-plant"></i>
                    Desafio
                </a>
            </li>
            <li class="menu-item">
                <a href="participantes.html">
                    <i class="ph ph-users"></i>
                    Participantes
                </a>
            </li>
        </ul>
    </header>

    <main class="main-content">
        <!-- Swiper -->
        <div class="swiper mySwiper">
            <div class="swiper-wrapper">
                {slides_html}
            </div>
            <div class="swiper-button-next"></div>
            <div class="swiper-button-prev"></div>
            <div class="swiper-pagination"></div>
        </div>
    </main>

    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@10/swiper-bundle.min.js"></script>
    <script>
        var swiper = new Swiper(".mySwiper", {{
            spaceBetween: 0,
            effect: "fade",
            loop: true,
            pagination: {{
                el: ".swiper-pagination",
                clickable: true,
            }},
            navigation: {{
                nextEl: ".swiper-button-next",
                prevEl: ".swiper-button-prev",
            }},
            autoplay: {{
                delay: 5000,
                disableOnInteraction: false,
            }}
        }});
    </script>
</body>
</html>
"""

with open('tema.html', 'w', encoding='utf-8') as f:
    f.write(new_tema_html)

print("Updated tema.html successfully!")
