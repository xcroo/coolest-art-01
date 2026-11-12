# Coolest art entry: copy the image beside this file to /output/entry.png.
# The image is a generated surreal scene: a giant glowing jellyfish over a neon city.
import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.png"))
