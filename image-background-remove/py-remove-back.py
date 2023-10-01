# Usage: python3 py-remove-back.py arg1,arg2,arg3
# Where argX is a list of images

from rembg import remove
from PIL import Image
import sys
images = sys.argv[1].split(',')
for image in images:
    input_path = image
    output_path = 'output_'+image+'.png'
    print(input_path)
    print(output_path)
    input = Image.open(input_path)
    output = remove(input)
    output.save(output_path)