# Genera los iconos de la PWA: un maki visto desde arriba
from PIL import Image, ImageDraw

def maki(tam, margen_extra=0.0):
    img = Image.new("RGBA", (tam, tam), (21, 21, 26, 255))
    d = ImageDraw.Draw(img)
    c = tam / 2
    # radio del maki (deja margen; más margen si es maskable)
    r = tam * (0.42 - margen_extra)
    # alga nori (exterior, casi negro verdoso)
    d.ellipse([c - r, c - r, c + r, c + r], fill=(30, 38, 30, 255))
    # arroz
    r2 = r * 0.80
    d.ellipse([c - r2, c - r2, c + r2, c + r2], fill=(242, 240, 236, 255))
    # granos de arroz insinuados
    import math, random
    random.seed(7)
    for i in range(26):
        ang = random.uniform(0, 2 * math.pi)
        rad = random.uniform(r * 0.45, r * 0.74)
        x, y = c + rad * math.cos(ang), c + rad * math.sin(ang)
        g = r * 0.055
        d.ellipse([x - g, y - g * 0.6, x + g, y + g * 0.6], fill=(228, 225, 218, 255))
    # salmón (centro)
    r3 = r * 0.38
    d.ellipse([c - r3, c - r3, c + r3, c + r3], fill=(232, 122, 77, 255))
    # vetas del salmón
    for i in (-1, 0, 1):
        y0 = c + i * r3 * 0.45
        d.arc([c - r3 * 0.85, y0 - r3 * 0.5, c + r3 * 0.85, y0 + r3 * 0.5],
              200, 340, fill=(245, 168, 130, 255), width=max(2, tam // 128))
    # toque de aguacate
    r4 = r3 * 0.30
    d.ellipse([c + r3 * 0.55 - r4, c - r3 * 0.75 - r4, c + r3 * 0.55 + r4, c - r3 * 0.75 + r4],
              fill=(118, 168, 87, 255))
    return img

maki(512).save(r"icons/icon-512.png")
maki(512).resize((192, 192), Image.LANCZOS).save(r"icons/icon-192.png")
maki(512, margen_extra=0.10).save(r"icons/icon-maskable-512.png")
print("Iconos creados")
