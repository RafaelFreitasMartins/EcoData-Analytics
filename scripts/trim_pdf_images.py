from PIL import Image, ImageChops

def trim(im):
    # Convert to RGB to avoid alpha channel issues with getpixel
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
        alpha = im.convert('RGBA').split()[-1]
        bg = Image.new("RGBA", im.size, (255,255,255,255))
        bg.paste(im, mask=alpha)
        im = bg.convert('RGB')
    else:
        im = im.convert('RGB')
        
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

images = ["PDF/images/pagina_1.jpg", "PDF/images/pagina_3.jpg", "PDF/images/pagina_4.jpg"]

for img_path in images:
    im = Image.open(img_path)
    trimmed = trim(im)
    # Save over the original
    trimmed.save(img_path, quality=95)
    print(f"Trimmed and saved {img_path}")
