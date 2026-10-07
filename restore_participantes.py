import re

with open('participantes.html', 'r', encoding='utf-8') as f:
    content = f.read()

missing_css = """
        .page-content {
            flex: 1;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        
        .header-title {
            text-align: center;
            margin-bottom: 40px;
        }
        
        .header-title h1 {
            font-size: 2.2rem;
            color: #1b5e20;
            margin-bottom: 10px;
        }
        
        .header-title p {
            font-size: 1.1rem;
            color: #555;
        }

        .cards-row {
            display: flex;
            gap: 30px;
            justify-content: center;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }

        .profile-card {
            width: 300px;
            background: #fff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            position: relative;
            transition: transform 0.3s;
        }

        .profile-card:hover {
            transform: translateY(-5px);
        }

        .profile-img {
            width: 100%;
            height: 350px;
            object-fit: cover;
            display: block;
        }

        .profile-gradient {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 150px;
            background: linear-gradient(transparent, rgba(0,0,0,0.8));
        }

        .profile-content {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 20px;
            color: #fff;
            text-align: center;
        }

        .profile-content h3 {
            font-size: 1.1rem;
            margin-bottom: 5px;
            text-transform: uppercase;
        }

        .profile-content p {
            font-size: 0.85rem;
            color: #ddd;
            margin-bottom: 15px;
        }

        .profile-socials {
            display: flex;
            justify-content: center;
            gap: 15px;
        }

        .profile-socials a {
            color: #fff;
            font-size: 24px;
            transition: color 0.2s;
        }

        .profile-socials a:hover {
            color: #4CAF50;
        }
"""

content = content.replace('.main-content {\n            flex: 1;', missing_css)

with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored CSS for participantes.html")
