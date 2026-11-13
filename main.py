"""ai-happy-01 entry: copy entry.jpg to /output/entry.png, deterministically.

The image is a warm storybook scene: a small friendly robot offers a
handmade birthday cake to a delighted grandmother in a golden-lit kitchen.
No network, no randomness: the same input bytes produce the same output
bytes on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SRC, dst)
# Sanity check: the output must be byte-identical to the source image.
assert os.path.getsize(dst) == os.path.getsize(SRC), "output size mismatch"
