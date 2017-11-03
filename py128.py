import sys
from hubarcode.code128 import Code128Encoder
import io
import numpy as np
from PIL import Image
import time
millis = int(round(time.time() * 1000))

def imggen(code):
	encoder = Code128Encoder(code, options={'bottom_border':10})  #'width':500
	#encoder.save("test.png")

	dm_in_bytes = io.BytesIO(encoder.get_imagedata())
	img = Image.open(dm_in_bytes)
	return img


def pil_grid(images, max_horiz=5):
    n_images = len(images)
    n_horiz = 5# min(n_images, max_horiz)
    h_sizes, v_sizes = [0] * n_horiz, [0] * (n_images // n_horiz)
    for i, im in enumerate(images):
        h, v = i % n_horiz, i // n_horiz
        h_sizes[h] = max(h_sizes[h], im.size[0])
        v_sizes[v] = max(v_sizes[v], im.size[1])
    h_sizes, v_sizes = np.cumsum([0] + h_sizes), np.cumsum([0] + v_sizes)
    im_grid = Image.new('L', (h_sizes[-1], v_sizes[-1]), color='white')
    for i, im in enumerate(images):
        im_grid.paste(im, (h_sizes[i % n_horiz], v_sizes[i // n_horiz]))
    return im_grid


finarray=[]
for i in range(98700000004000000000,98700000004000000100):
	finarray.append(imggen(str(i)))

image_file = pil_grid(finarray,2).convert('1')
image_file.save('result.png')

print ("ready. Time consumpted="+str((int(round(time.time() * 1000))-millis)/1000)+" seconds")