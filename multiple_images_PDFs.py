from PIL import Image
from pathlib import Path
import os

path = os.getcwd()

for file in Path(path).iterdir():
  if(str(file).lower().endswith('.jpeg') or str(file).lower().endswith('.png') or str(file).lower().endswith('.jpg')):
    image = Image.open(str(file))
    img = image.convert('RGB')
    img.save(file.stem + '.pdf')
