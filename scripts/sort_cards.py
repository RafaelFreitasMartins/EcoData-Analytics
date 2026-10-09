from bs4 import BeautifulSoup

# 1. Update participantes.html
with open('participantes.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

cards = soup.find_all('div', class_='profile-card')
if cards:
    # Get the parent of the first card (likely a cards-row)
    # Actually, they might be in multiple <div class="cards-row">.
    # Let's extract all cards, sort them, and put them back in a single cards-row or multiple.
    cards_data = []
    for card in cards:
        name_tag = card.find('h3')
        name = name_tag.text.strip().lower() if name_tag else ""
        # Also clean up the HTML of the card just to be safe
        cards_data.append((name, card))

    cards_data.sort(key=lambda x: x[0])
    
    # Remove all existing cards-row
    rows = soup.find_all('div', class_='cards-row')
    parent = rows[0].parent if rows else None
    
    if parent:
        for row in rows:
            row.decompose()
            
        # Group cards by 3 per row (or 4, based on original)
        # Let's just put 3 per row
        for i in range(0, len(cards_data), 3):
            new_row = soup.new_tag('div', attrs={'class': 'cards-row'})
            for _, card in cards_data[i:i+3]:
                new_row.append(card)
            parent.append(new_row)

    with open('participantes.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

logo = soup.find('img', class_='logo')
if logo:
    # Use the transparent logo we created
    logo['src'] = 'Logo novo_transparent.png'
    # Remove the mix-blend-mode if it's there, because the transparent PNG doesn't need it
    if 'style' in logo.attrs:
        logo['style'] = logo['style'].replace('mix-blend-mode: multiply;', '').strip()
        if not logo['style']:
            del logo['style']

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Modifications done.")
