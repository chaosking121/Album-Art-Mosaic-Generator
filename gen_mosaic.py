import os
import math
import random
from PIL import Image

image_dir = 'pics/'
image_dim = 500
image_dim_small = 100

if __name__ == '__main__':
    path_list = [os.path.join(image_dir, f) for f in sorted(os.listdir(image_dir))]
    random.shuffle(path_list)

    side_length = math.floor(math.sqrt(len(path_list)))

    images = [Image.open(x) for x in path_list]

    mosaic = Image.new('RGB', (side_length * image_dim, side_length * image_dim))

    for row in range(side_length):
        for col in range(side_length):
             mosaic.paste(images[(row * side_length) + col], (col * image_dim, row * image_dim))


    mosaic.save('mosaic.png')

    mosaic = mosaic.resize((side_length * image_dim_small, side_length * image_dim_small), Image.ANTIALIAS)
    mosaic.save('mosaic_small.png')