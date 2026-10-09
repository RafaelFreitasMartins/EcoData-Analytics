import re

with open('pdf.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Current container inline style:
# style="padding: 20px; max-width: 800px; display: flex; align-items: center; justify-content: center; height: 90vh;"
old_container_style = r'style="padding: 20px; max-width: 800px; display: flex; align-items: center; justify-content: center; height: 90vh;"'
new_container_style = 'style="padding: 20px; max-width: 1200px; display: flex; align-items: flex-start; justify-content: center; height: 90vh; overflow-y: auto;"'

# Current image inline style:
# style="max-height: 100%; max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);"
old_img_style = r'style="max-height: 100%; max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);"'
new_img_style = 'style="width: 100%; max-width: 1000px; height: auto; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);"'

content = re.sub(old_container_style, new_container_style, content)
content = re.sub(old_img_style, new_img_style, content)

with open('pdf.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated PDF image sizing.")
