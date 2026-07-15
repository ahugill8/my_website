#!/usr/bin/env python3
"""Generates labeled SVG placeholder images for the site.
Run once during scaffolding; safe to re-run (overwrites placeholders only)."""

import os
from xml.sax.saxutils import escape

BASE = os.path.join(os.path.dirname(__file__), "..", "images")

PALETTE = {
    "cream": "#F4EEE2",
    "cream2": "#EDE4D3",
    "ink": "#2B2A28",
    "red": "#B3271C",
    "line": "#C9BFA8",
}

def svg_rect(path, w, h, label, sublabel="", shape="rect", bg=None, fg=None):
    label = escape(label)
    sublabel = escape(sublabel)
    bg = bg or PALETTE["cream2"]
    fg = fg or PALETTE["ink"]
    rx = 18 if shape == "rect" else min(w, h) / 2
    clip = f'<clipPath id="clip"><rect x="0" y="0" width="{w}" height="{h}" rx="{rx}"/></clipPath>' if shape != "circle" else f'<clipPath id="clip"><circle cx="{w/2}" cy="{h/2}" r="{min(w,h)/2}"/></clipPath>'
    shape_el = (f'<rect x="0" y="0" width="{w}" height="{h}" rx="{rx}" fill="{bg}"/>'
                if shape != "circle" else
                f'<circle cx="{w/2}" cy="{h/2}" r="{min(w,h)/2}" fill="{bg}"/>')
    dash = (f'<rect x="6" y="6" width="{w-12}" height="{h-12}" rx="{max(rx-6,0)}" '
            f'fill="none" stroke="{PALETTE["line"]}" stroke-width="2" stroke-dasharray="10 8"/>'
            if shape != "circle" else
            f'<circle cx="{w/2}" cy="{h/2}" r="{min(w,h)/2-6}" fill="none" stroke="{PALETTE["line"]}" stroke-width="2" stroke-dasharray="10 8"/>')
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  {shape_el}
  {dash}
  <text x="{w/2}" y="{h/2 - (10 if sublabel else 0)}" text-anchor="middle" dominant-baseline="middle"
        font-family="Georgia, 'Times New Roman', serif" font-size="{max(14, min(w,h)//14)}" fill="{fg}">{label}</text>
  {f'<text x="{w/2}" y="{h/2+22}" text-anchor="middle" dominant-baseline="middle" font-family="Georgia, serif" font-size="{max(11, min(w,h)//22)}" fill="{fg}" opacity="0.7">{sublabel}</text>' if sublabel else ''}
</svg>'''
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(svg)

# Home
svg_rect(f"{BASE}/home/headshot.svg", 560, 560, "Your Headshot", "square or circle crop, high-res", shape="circle")
svg_rect(f"{BASE}/home/grad-photo.svg", 380, 480, "Columbia", "Graduation Photo")
svg_rect(f"{BASE}/home/betsy-bernie.svg", 380, 480, "Betsy & Bernie")
svg_rect(f"{BASE}/home/notepad.svg", 380, 480, "Notepad", "scribbled writing, close-up")

# About
svg_rect(f"{BASE}/about/ticket.svg", 620, 260, "Old Ticket", "Name / Hometown")
svg_rect(f"{BASE}/about/columbia-video-poster.svg", 640, 360, "Columbia Video", "poster frame / thumbnail")

# Publications — 6 logo placeholders
for i in range(1, 7):
    svg_rect(f"{BASE}/publications/logo-{i}.svg", 200, 200, f"Logo {i}", "click to link", shape="circle")

# Editorial
svg_rect(f"{BASE}/editorial/hero.svg", 900, 420, "Editorial", "hero image or sample spread")

# CV
svg_rect(f"{BASE}/cv/portrait.svg", 320, 400, "CV Portrait", "optional")

# Contact
svg_rect(f"{BASE}/contact/photobooth.svg", 340, 620, "Photo Booth", "strip photo")

print("Placeholders generated.")
