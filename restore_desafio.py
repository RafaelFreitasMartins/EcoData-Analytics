import re

with open('desafio.html', 'r', encoding='utf-8') as f:
    content = f.read()

missing_css = """
        .page-content {
            flex: 1;
            padding: 40px;
            max-width: 1200px;
            margin: 0 auto;
            width: 100%;
            overflow-y: auto;
        }

        .header-title {
            text-align: center;
            margin-bottom: 30px;
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

        .missao-box {
            background-color: #e8f5e9;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 40px;
            color: #1b5e20;
            border-left: 5px solid #2e7d32;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 30px;
            justify-content: center;
        }

        .flip-card {
            background-color: transparent;
            width: 100%;
            height: 380px;
            perspective: 1000px;
        }

        .flip-card-inner {
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }

        .flip-card:hover .flip-card-inner {
            transform: rotateY(180deg);
        }

        .flip-card-front, .flip-card-back {
            position: absolute;
            width: 100%;
            height: 100%;
            -webkit-backface-visibility: hidden;
            backface-visibility: hidden;
            border-radius: 12px;
            padding: 30px;
            display: flex;
            flex-direction: column;
        }

        .flip-card-front {
            background-color: #1a1a1a;
            color: white;
            align-items: center;
            justify-content: center;
        }

        .flip-card-front i {
            font-size: 64px;
            margin-bottom: 20px;
            color: #4CAF50;
        }

        .flip-card-front h3 {
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 10px;
            color: #ffffff;
        }

        .flip-card-front p {
            font-size: 0.95rem;
            color: #999999;
            margin: 0;
        }

        .flip-card-back {
            background-color: #ffffff;
            color: #333333;
            transform: rotateY(180deg);
            border-top: 6px solid #4CAF50;
            overflow-y: auto;
            text-align: left;
            align-items: flex-start;
            justify-content: flex-start;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }

        .flip-card-back::-webkit-scrollbar { width: 6px; }
        .flip-card-back::-webkit-scrollbar-thumb { background-color: #ccc; border-radius: 4px; }

        .question {
            font-size: 1.1rem;
            color: #222;
            font-weight: bold;
            margin-top: 0;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid #eee;
            line-height: 1.4;
        }

        .answer {
            color: #444;
            font-size: 0.95rem;
            line-height: 1.6;
        }

        .answer-highlight {
            margin-top: 15px;
            padding: 15px;
            background-color: #f5f8f5;
            border-left: 4px solid #4CAF50;
            border-radius: 4px;
            font-size: 0.9rem;
            color: #1b5e20;
        }
"""

content = content.replace('.main-content {\n            flex: 1;', missing_css)

with open('desafio.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Restored CSS for desafio.html")
