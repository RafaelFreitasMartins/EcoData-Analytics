import re

with open('powerbi.html', 'r', encoding='utf-8') as f:
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
        }

        .header-title {
            text-align: center;
            margin-bottom: 20px;
        }

        .header-title h1 {
            color: #1b5e20;
            font-size: 2.2rem;
            margin-bottom: 10px;
        }
        
        .header-title p {
            color: #555;
            font-size: 1.1rem;
        }

        .iframe-container {
            flex: 1;
            width: 100%;
            height: 100%;
            min-height: 600px;
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            overflow: hidden;
            display: flex;
        }

        .iframe-container iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
"""

content = content.replace('.main-content {\n            flex: 1;', missing_css)

with open('powerbi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored CSS for powerbi.html")
