import os
import cairosvg

input_folder = "svg_pieces"
output_folder = "assets"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Convert all SVGs to PNGs
for file in os.listdir(input_folder):
    if file.endswith(".svg"):
        svg_file = os.path.join(input_folder, file)
        png_file = os.path.join(output_folder, file.replace(".svg", ".png"))
        cairosvg.svg2png(url=svg_file, write_to=png_file, output_width=60, output_height=60)

print("✅ All SVGs converted to PNGs in 'assets/' folder.")
