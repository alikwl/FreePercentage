import os
from PIL import Image, ImageDraw, ImageFont

base_dir = r"E:\websites\freepercentage"
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)

# 1. Favicon (512x512)
fav = Image.new('RGB', (512, 512), color='#0056b3')
draw = ImageDraw.Draw(fav)
try:
    font_large = ImageFont.truetype("arial.ttf", 350)
    font_medium = ImageFont.truetype("arial.ttf", 100)
except:
    font_large = ImageFont.load_default()
    font_medium = ImageFont.load_default()

draw.text((256, 256), "%", fill="#ff6b00", font=font_large, anchor="mm")
fav.save(os.path.join(assets_dir, "favicon.png"))

# Logo (Horizontal)
logo = Image.new('RGBA', (1200, 300), color=(255, 255, 255, 0))
d_logo = ImageDraw.Draw(logo)
# rounded rect trick? just draw a square
d_logo.rounded_rectangle([(20, 20), (280, 280)], radius=40, fill='#0056b3')
d_logo.text((150, 150), "%", fill="#ff6b00", font=font_large, anchor="mm")
d_logo.text((320, 150), "FreePercentage.com", fill="#1a1a2e", font=ImageFont.truetype("arial.ttf", 150) if "truetype" in str(font_large) else font_medium, anchor="lm")
logo.save(os.path.join(assets_dir, "logo.png"))

# OG Image
og = Image.new('RGB', (1200, 630), color='#1a1a2e')
d_og = ImageDraw.Draw(og)
d_og.rounded_rectangle([(500, 100), (700, 300)], radius=40, fill='#0056b3')
d_og.text((600, 200), "%", fill="#ff6b00", font=font_large, anchor="mm")
d_og.text((600, 420), "FreePercentage.com", fill="#ffffff", font=font_medium, anchor="mm")
d_og.text((600, 520), "Fast, Accurate, Free Calculators", fill="#aab4c8", font=ImageFont.truetype("arial.ttf", 60) if "truetype" in str(font_large) else font_medium, anchor="mm")
og.save(os.path.join(assets_dir, "og-image.png"))

print("Images generated successfully.")