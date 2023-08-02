import numpy as np
# import skimage
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import os
import scipy.misc as sm
import cv2

def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

def load_data():    
    '''
    Load images from the "assets" directory
    Images are in JPG and we convert it to gray scale images
    '''
    cwd=os.getcwd()
    dir_name= os.path.join(cwd, "assets")
    imgs = []
    for filename in os.listdir(dir_name):
        if os.path.isfile(dir_name + '/' + filename):
            img = mpimg.imread(dir_name + '/' + filename)
            img = rgb2gray(img)
            imgs.append(img)
    return imgs


def visualize(imgs, format=None, gray=False):
    plt.figure(figsize=(20, 40))
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1,2,0)
        plt_idx = i+1
        plt.subplot(2, 2, plt_idx)
        plt.imshow(img, format)
    plt.show()

def save_image(imgs):
    for i, img in enumerate(imgs):
        name='out'+str(i)+'.png'
        path=os.path.join(os.getcwd(), "results", name)
        cv2.imwrite(path, img)
        print('Image saved at : ', path)
