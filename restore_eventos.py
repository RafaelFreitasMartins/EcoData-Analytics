import re

with open('eventos.html', 'r', encoding='utf-8') as f:
    content = f.read()

missing_css = """
        .page-content {
            flex: 1;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
        }

        .title-section {
            text-align: center;
            margin-bottom: 40px;
        }

        .title-section h1 {
            color: #1b5e20;
            font-size: 2.2rem;
            margin-bottom: 10px;
        }

        .title-section p {
            color: #555;
            font-size: 1.1rem;
        }

        .phenomenon-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 40px;
        }

        .card {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            border-top: 6px solid #ccc;
        }
        
        .card.nino {
            border-top-color: #e74c3c;
        }

        .card.nino h2 {
            color: #e74c3c;
        }

        .card.nina {
            border-top-color: #3498db;
        }

        .card.nina h2 {
            color: #3498db;
        }

        .card h2 {
            font-size: 1.8rem;
            margin-bottom: 15px;
        }

        .card p {
            color: #444;
            line-height: 1.6;
            margin-bottom: 20px;
        }

        .impact {
            background-color: #f9fbf9;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #4CAF50;
            color: #333;
            font-size: 0.95rem;
            line-height: 1.5;
        }

        @media (max-width: 768px) {
            .phenomenon-grid {
                grid-template-columns: 1fr;
            }
        }
"""

content = content.replace('.main-content {\n            flex: 1;', missing_css)

with open('eventos.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored CSS for eventos.html")
