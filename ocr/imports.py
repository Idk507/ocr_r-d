import cv2
import shutil
import imutils
from imutils import contours
from PIL import Image
import numpy as np
import os
# import tesserocr as tr
import pytesseract as tr 
import re 
import os 
import io 
from google.cloud import vision 
from matplotlib import pyplot as plt 
import pandas as pd 
from skimage.segmentation import clear_border
from imutils import contours
from keras.models import load_model


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\danus\miniconda3\envs\yolov4-gpu\Lib\site-packages\pytesseract'
charNames = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "T", "U", "A", "D"]
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (17, 7))
mnist_model = load_model('./../mnist_GC_v1.h5')

