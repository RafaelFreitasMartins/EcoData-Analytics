from PIL import Image

# Open the image and convert to RGBA
img = Image.open('Logo novo.png').convert('RGBA')

# Get the data
data = img.getdata()
new_data = []

for item in data:
    # Change all black (also shades of black)
    # to transparent
    if item[0] < 30 and item[1] < 30 and item[2] < 30:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

# Update image data
img.putdata(new_data)

# Save new image
img.save('Logo novo_transparent.png')
print("Image background removed.")
