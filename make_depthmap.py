from PIL import Image
import numpy as np
import cv2

disp_file = "./cityscape_testdepthimg.png"
depth_img = "./000464.png"
disp = cv2.imread(disp_file, cv2.IMREAD_UNCHANGED).astype(np.float32)   # read the 16-bit disparity png file
#disp += 0.0001
disp[disp > 0] = (disp[disp > 0] - 1) / 256    # convert the png file to real disparity values, according to the official documentation.
# you could also refer to https://github.com/mcordts/cityscapesScripts/issues/55#issuecomment-411486510

# read camera parameters
focal = 2262.52
baseline = 0.209313

depth = baseline * focal / disp
depth[depth == np.inf] = 0
depth[depth == np.nan] = 0

cv2.imwrite("cityscape_depth.png", depth)