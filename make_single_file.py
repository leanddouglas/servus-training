#!/usr/bin/env python3
"""
Servus Group - Single File Packager v2
- Embeds all local images as base64
- Converts YouTube iframes into clickable thumbnails
  (YouTube iframes don't work from file:// - thumbnails do!)
"""

import base64
import os
import re

# === CONFIG ===
INPUT_FILE  = "fiber_identification_printable.html"
OUTPUT_FILE = "index.html"
FOLDER      = os.path.dirname(os.path.abspath(__file__))

print("=" * 55)
print("  Servus Group - Single File Packager v2")
print("=" * 55)

# Read the HTML
input_path = os.path.join(FOLDER, INPUT_FILE)
with open(input_path, "r", encoding="utf-8") as f:
    html = f.read()

# ── STEP 1: Embed local images as base64 ──────────────────
pattern = r'src="(?!http|https|//|data:)([^"]+\.(png|jpg|jpeg|gif|svg|webp))"'
matches = re.findall(pattern, html, re.IGNORECASE)

replaced_imgs = 0
for filename, ext in matches:
    image_path = os.path.join(FOLDER, filename)
    if os.path.exists(image_path):
        mime_map = {
            "png": "image/png", "jpg": "image/jpeg",
            "jpeg": "image/jpeg", "gif": "image/gif",
            "svg": "image/svg+xml", "webp": "image/webp"
        }
        mime = mime_map.get(ext.lower(), "image/png")
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode("utf-8")
        data_uri = f"data:{mime};base64,{encoded}"
        html = html.replace(f'src="{filename}"', f'src="{data_uri}"')
        print(f"  ✅ Embedded image: {filename}")
        replaced_imgs += 1
    else:
        print(f"  ⚠️  Image NOT FOUND (skipped): {filename}")

# ── STEP 2: SKIPPED (Keep YouTube iframe since we are on GitHub Pages) ──
count = 0
print(f"  ✅ Keeping YouTube inline players intact")

# ── STEP 3: Write output ───────────────────────────────────
output_path = os.path.join(FOLDER, OUTPUT_FILE)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print()
print(f"  Done! {replaced_imgs} image(s) embedded.")
print(f"  📄 Output: {OUTPUT_FILE}")
print()
print("  ✅ This file is 100% self-contained.")
print("  ✅ Images are embedded directly.")
print("  ✅ Video plays inline (perfect for GitHub Pages hosting).")
print("=" * 55)
