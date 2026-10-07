from bs4 import BeautifulSoup

# Open the file
with open('participantes.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

main_container = soup.find('main')
if main_container:
    # Extract all profile cards in order
    all_cards = soup.find_all('div', class_='profile-card')
    
    # Remove all existing cards-row containers
    for row in main_container.find_all('div', class_='cards-row'):
        row.decompose()
    
    # Create two new rows
    row1 = soup.new_tag('div', attrs={'class': 'cards-row'})
    row2 = soup.new_tag('div', attrs={'class': 'cards-row'})
    
    # Append first 3 to row1
    for card in all_cards[:3]:
        row1.append(card)
        
    # Append the rest (4) to row2
    for card in all_cards[3:]:
        row2.append(card)
        
    # Add rows back to main container
    main_container.append(row1)
    main_container.append(row2)

# Save the changes
with open('participantes.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Layout adjusted: 3 cards in row 1, 4 cards in row 2.")
