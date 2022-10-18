import argparse
import sys
import numpy as np
from PIL import Image
import cv2


def preprocess(original_pth, altered_pth):
    DEPTH_COEFF = 5000
    original = np.array(Image.open(original_pth)).astype(np.float32)
    original /= DEPTH_COEFF
    altered = np.array(Image.open(altered_pth)).astype(np.float32)
    altered /= DEPTH_COEFF
    original += 0.0001
    altered += 0.0001
    width = original.shape[0]
    height = original.shape[1]
    channel = original.shape[2]
    n = width * height

    return original, altered, n


def rel(original_pth, altered_pth):
    original, altered, n = preprocess(original_pth,altered_pth)
    print("AVERAGE RELATIVE ERROR (REL)")
    print((np.sum(np.abs(original - altered) / original)) / n)


def rms(original_pth, altered_pth):
    original, altered, n = preprocess(original_pth, altered_pth)
    print("ROOT MEAN SQUARED ERROR (RMS)")
    print(np.sqrt(np.sum((original - altered) ** 2) / n))


def rel(original_pth, altered_pth):
    original, altered, n = preprocess(original_pth, altered_pth)
    print("AVERAGE (LOG10) ERROR")
    print(np.sum(np.abs(np.log10(original) - np.log10(altered))) / n)


def all_metrics(original_pth, altered_pth):
    original, altered, n = preprocess(original_pth, altered_pth)
    print("AVERAGE RELATIVE ERROR (REL)")
    print((np.sum(np.abs(original - altered) / original)) / n)
    print("ROOT MEAN SQUARED ERROR (RMS)")
    print(np.sqrt(np.sum((original - altered) ** 2) / n))
    print("AVERAGE (LOG10) ERROR")
    print(np.sum(np.abs(np.log10(original) - np.log10(altered))) / n)