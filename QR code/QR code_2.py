import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask

# --- 1. DATA & PALETTE ---
vcard = (
    "BEGIN:VCARD\nVERSION:3.0\n"
    "FN:Your Name\nTEL;TYPE=CELgit commit -m L:Your Phone Number\n"
    "ORG:Airtel Interior Premium\nEND:VCARD"
)

DEEP_SPACE = (4, 12, 10, 255)
GLOW_TEAL = (0, 255, 180, 45)
MINT_FROST = (180, 255, 230, 255)
SILK_PEARL = (245, 250, 250, 255)

# --- 2. QR CORE GENERATION ---
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=22, border=4)
qr.add_data(vcard)
qr.make(fit=True)

img_styled = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),
    eye_drawer=RoundedModuleDrawer(radius_ratio=0.9),
    color_mask=VerticalGradiantColorMask(
        back_color=(4, 12, 10),
        top_color=(0, 230, 160),
        bottom_color=(0, 110, 85)
    )
)

img = img_styled.convert("RGBA")
qr_w, qr_h = img.size

# --- 3. THE LUXURY CANVAS ---
footer_h = 160
canvas = Image.new("RGBA", (qr_w, qr_h + footer_h), DEEP_SPACE)

glow = Image.new("RGBA", (qr_w, qr_h), (0, 0, 0, 0))
g_draw = ImageDraw.Draw(glow)
g_draw.ellipse([qr_w//4, qr_h//4, 3*qr_w//4, 3*qr_h//4], fill=GLOW_TEAL)
glow = glow.filter(ImageFilter.GaussianBlur(radius=90))
canvas.paste(glow, (0, 0), glow)

canvas.paste(img, (0, 0), img)
draw = ImageDraw.Draw(canvas)

# --- 4. TYPOGRAPHY & BRANDING ---
try:
    font_name = ImageFont.truetype("timesbd.ttf", 54)
    font_scan = ImageFont.truetype("arialbd.ttf", 32)
except:
    font_name = font_scan = ImageFont.load_default()

margin_right = 90
instr_text = "S C A N  •  T O  •  C O N T A C T"
name_text = "Your Name"
tw_scan = draw.textbbox((0, 0), instr_text, font=font_scan)[2]
tw_name = draw.textbbox((0, 0), name_text, font=font_name)[2]

scan_x, scan_y = qr_w - tw_scan - margin_right, qr_h - 45
name_x, name_y = qr_w - tw_name - margin_right, scan_y + 35

for off in range(1, 3):
    draw.text((name_x + off, name_y + off), name_text, fill=(0, 15, 10, 150), font=font_name)

draw.text((scan_x, scan_y), instr_text, fill=MINT_FROST, font=font_scan)
draw.text((name_x, name_y), name_text, fill=SILK_PEARL, font=font_name)

# --- 5. LOGO (Seamless Contact Avatar - NEW) ---
cx, cy = qr_w // 2, qr_h // 2

# Clearing center area to match QR background
draw.ellipse([cx-70, cy-70, cx+70, cy+70], fill=DEEP_SPACE)

# Outer Ring Accent
draw.ellipse([cx-60, cy-60, cx+60, cy+60], outline=(0, 230, 160, 180), width=2)

# Avatar Head
draw.ellipse([cx-18, cy-35, cx+18, cy+2], fill=MINT_FROST)
# Avatar Shoulders
draw.chord([cx-38, cy-5, cx+38, cy+48], start=180, end=0, fill=MINT_FROST)

# --- 5.5 ARCHITECTURAL FRAME ---
border_color = (0, 150, 120, 180)
accent_line = (180, 255, 230, 150)
draw.rectangle([15, 15, qr_w - 15, qr_h + footer_h - 15], outline=border_color, width=2)
length = 40
draw.line([25, 25+length, 25, 25, 25+length, 25], fill=accent_line, width=4)
draw.line([qr_w-25-length, qr_h+footer_h-25, qr_w-25, qr_h+footer_h-25, qr_w-25, qr_h+footer_h-25-length], fill=accent_line, width=4)

# --- 6. EXPORT ---
canvas = canvas.convert("RGB")
canvas.save("QR_Contact_Final.jpg", quality=100, subsampling=0)

print("✨ Success. Logo updated to Contact Icon with seamless background.")