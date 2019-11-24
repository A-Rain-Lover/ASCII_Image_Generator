import skimage
from skimage import data
from skimage.io import imread

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import argparse as ap

parser = ap.ArgumentParser()
parser.add_argument("input",type=str,help="Path to the input image file.")
parser.add_argument("output",type=str,help="Path where to put the output file.")
args = parser.parse_args()


img = imread(args.input,as_gray=True)

txt = open(args.output,'w+')

h = len(img)
w = len(img[0])

n = 20
_img = skimage.transform.downscale_local_mean(img,(n,n))

chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
for i in range(len(_img)):
    for j in range(len(_img[0])):
        txt.write(chars[int(_img[i,j]*len(chars)-1)]+' ')
    txt.write('\n')

print("")
