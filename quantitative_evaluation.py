import argparse
import sys
import numpy as np
from PIL import Image
import cv2


def main(original_pth, altered_pth, evaluation):
    original = np.array(Image.open(original_pth)).astype(np.float32)
    altered = np.array(Image.open(altered_pth)).astype(np.float32)
    original += 0.001
    altered  += 0.001
    width = original.shape[0]
    height = original.shape[1]
    channel = original.shape[2]
    n = width * height

    if evaluation == 0:
        print("AVERAGE RELATIVE ERROR (REL)")
        print( ( np.sum( np.abs(original - altered) / original ) ) / n )
    elif evaluation == 1:
        print("ROOT MEAN SQUARED ERROR (RMS)")
        print( np.sqrt( np.sum( (original - altered) ** 2 ) / n ) )
    elif evaluation == 2:
        print("AVERAGE (LOG10) ERROR")
        print( np.sum( np.abs(np.log10(original) - np.log10(altered) ) )/ n )
    else:
        print("AVERAGE RELATIVE ERROR (REL)")
        print((np.abs(original - altered) / original) / n)
        print("ROOT MEAN SQUARED ERROR (RMS)")
        print(np.sqrt(((original - altered) ** 2) / n))
        print("AVERAGE (LOG10) ERROR")
        print(np.abs(np.log10(original) - np.log10(altered)) / n)

main("./nyud_testimg.png", "./nyud_testdepthimg.png", 0)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='QUANTITATIVE EVALUATION BETWEEN TWO IMAGES')
#     parser.add_argument('--org', type=str, required=True, help="The path to the original image.")
#     parser.add_argument('--alt', type=str, required=True, help="The path to the altered image.")
#     parser.add_argument('--eval', type=int, required=True, help="0: Average Relative Error (REL) 1: Root Mean Squared Error (RMS) 2: Average (log10) Error 3: All Evaluations")
#     args = parser.parse_args()
#     main(args.org, args.alt, args.eval)