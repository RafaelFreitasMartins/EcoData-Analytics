from PIL import Image, ImageChops

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

images = ["PDF/images/pagina_1.jpg", "PDF/pd_tela_segunda_tela.png", "PDF/images/pagina_3.jpg", "PDF/images/pagina_4.jpg"]

for img_path in images:
    im = Image.open(img_path)
    old_size = im.size
    trimmed = trim(im)
    new_size = trimmed.size
    print(f"{img_path}: {old_size} -> {new_size}")
    # Don't save yet, just checking
