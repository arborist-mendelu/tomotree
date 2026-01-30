from PIL import Image

# Načti obrázek
img = Image.open("woodu.png").convert("RGBA")

# Vytvoř nové neprůhledné pozadí (např. bílé)
background = Image.new("RGBA", img.size, (255, 255, 255, 255))

# Slouč vrstvy – průhledná místa se nahradí pozadím
composite = Image.alpha_composite(background, img)

# Ulož jako obyčejný RGB obrázek (bez alfa kanálu)
composite.convert("RGB").save("bez_pruhlednosti.png")