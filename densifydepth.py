import csv
import numpy as np
import imageio
import os
from PIL import Image
from fill_depth_colorization import fill_depth_colorization


read_from = "./kittit_train.csv"
with open(read_from, 'r') as read:
    csvreader = csv.reader(read)
    i = 1
    for row in csvreader:
        print("{}/85848".format(i))
        depth = np.array(Image.open(row[2])).astype(np.float32)
        image = np.array(Image.open(row[1])).astype(np.float32)
        output = fill_depth_colorization(image, depth, alpha=1)
        os.remove(row[2])
        imageio.imwrite(row[2], output.astype(np.uint16))
        i += 1