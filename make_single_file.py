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

# ── STEP 2: Replace YouTube iframes with clickable thumbnails ──
# Matches <iframe src="https://www.youtube.com/embed/VIDEO_ID" ...></iframe>
youtube_pattern = re.compile(
    r'<iframe[^>]+src="https://www\.youtube\.com/embed/([a-zA-Z0-9_-]+)"[^>]*>\s*</iframe>',
    re.DOTALL
)

def make_youtube_thumbnail(match):
    video_id = match.group(1)
    watch_url = f"https://www.youtube.com/watch?v={video_id}"
    thumb_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    return f'''<div style="text-align:center; margin: 10px 0; position: relative; display: inline-block; width: 100%; max-width: 700px;">
  <a href="{watch_url}" target="_blank" rel="noopener" title="Click to watch video on YouTube"
     style="display:block; position:relative; cursor:pointer; border-radius:8px; overflow:hidden; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
    <img src="{thumb_url}" alt="Click to watch video" loading="lazy"
         style="width:100%; height:auto; display:block; border-radius:8px;">
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                background:rgba(255,0,0,0.88); border-radius:50%; width:72px; height:72px;
                display:flex; align-items:center; justify-content:center;">
      <svg viewBox="0 0 24 24" width="36" height="36" fill="white">
        <path d="M8 5v14l11-7z"/>
      </svg>
    </div>
  </a>
  <p style="margin-top:8px; font-size:0.85em; color:#555;">
    ▶ <a href="{watch_url}" target="_blank" style="color:#004085; font-weight:600;">Click to watch on YouTube</a>
  </p>
</div>'''

html, count = youtube_pattern.subn(make_youtube_thumbnail, html)

if count:
    print(f"  ✅ Converted {count} YouTube iframe(s) → clickable thumbnail")
else:
    print(f"  ℹ️  No YouTube iframes found to convert")

# ── STEP 3: Write output ───────────────────────────────────
output_path = os.path.join(FOLDER, OUTPUT_FILE)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html)

print()
print(f"  Done! {replaced_imgs} image(s) embedded, {count} video(s) converted.")
print(f"  📄 Output: {OUTPUT_FILE}")
print()
print("  ✅ This file is 100% self-contained.")
print("  ✅ Video thumbnail works from any file, email, WhatsApp.")
print("  ✅ Clicking the thumbnail opens YouTube on any device.")
print("=" * 55)
