import re

with open('powerbi.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_url = r'https://app\.powerbi\.com/reportEmbed\?reportId=[a-zA-Z0-9\-]+&autoAuth=true&ctid=[a-zA-Z0-9\-]+'
new_url = 'https://app.powerbi.com/reportEmbed?reportId=3582c810-464c-4832-b3ec-e094e2fdb549&autoAuth=true&ctid=bd697c1b-c481-479c-841e-c618542675c3'

content = re.sub(old_url, new_url, content)

with open('powerbi.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("PowerBI Dashboard URL updated.")
