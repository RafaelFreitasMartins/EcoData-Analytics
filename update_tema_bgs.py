import re

with open('tema.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all background-image: url(...) in swiper-slide to use amazon_river_hd.jpg
content = re.sub(r'background-image:\s*url\([^)]+\)', "background-image: url('amazon_river_hd.jpg')", content)

with open('tema.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated backgrounds in tema.html")
