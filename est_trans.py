##### !!!!!DO NOT CHANGE OR ADD ANY IMPORTS WITHOUT PERMISSION!!!!!
##### IMPORTS START #####
# Imported modules, do not change or add anything
import imageio, sys, os, numpy as np, zipfile, math
from tqdm import tqdm
from skimage.transform import warp
from skimage.transform import resize
import torch
import torch.nn as nn
try:
    from google.colab import drive
    os.system('pip install -U opencv-contrib-python==4.4.0.44')
    import cv2
    print(f'\ncv2 version: {cv2.__version__}\n')
    sift_testing_blah = cv2.SIFT_create(nOctaveLayers = 3, contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6)
except:
    import cv2
    sift_testing_blah = cv2.SIFT_create(nOctaveLayers = 3, contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6)
##### IMPORTS END #####



# Class you will be turning in
# DO NOT put any viewing functions in the class, do this in main.py
class estimate_transforms:
    # Constructor
    def __init__(self, img_path_reg, img_path_warped):
        # Open images
        self.img_reg = imageio.imread(img_path_reg)
        self.img_warped = imageio.imread(img_path_warped)


    
    ##### HELPERS SECTIONS #####
    ## Place any additional helpers here
    ## Dont need to use these, can create whatever you like

    ## QR Decomp
    def qr_solve(self, H, b):
        pass

    ## RANSAC
    def run_ransac(self, points_reg, points_warped, acceptable_error=2, min_samples=3, fraction_inlier=0.05):
        T = np.eye(3)
        re = 0.0

        return (T, re)

    ## Get SIFT Feature Point Pairs
    def get_sift_points(self, num_matches):
        points_reg = None
        points_warped = None

        return (points_reg, points_warped)

    ## Warp a
    def warp_a(self):
        pass

    ## Warp b
    def warp_b(self):
        pass

    ## Affine fit function
    def affine_fit(self, points_reg, points_warped):
        pass

    ## Rotation and translation fit function
    def rt_fit(self, points_reg, points_warped):
        pass

    ## Perspective/Projection fit function
    def perspective_fit(self, points_reg, points_warped):
        pass



    ##### STUDENTS SECTION #####
    ## Do not change the functions definition or return types

    ## Affine fit
    def fit_affine(self):
        # Can delete, just makes blank residual and Transform matrix
        points_reg, points_warped = self.get_sift_points(num_matches=8)
        T, re = self.run_ransac(points_reg, points_warped, self.affine_fit)

        # Dont change output/return
        return (T, re)

    ##  Rotation & Translation fit
    def fit_rotate_translation(self):
        # Can delete, just makes blank residual and Transform matrix
        points_reg, points_warped = self.get_sift_points(num_matches=8)
        T, re = self.run_ransac(points_reg, points_warped, self.rt_fit)

        # Dont change output/return
        return (T, re)

    ## Perspective/Projective fit
    def fit_perspective(self):
        # Can delete, just makes blank residual and Transform matrix
        points_reg, points_warped = self.get_sift_points(num_matches=8)
        T, re = self.run_ransac(points_reg, points_warped, self.perspective_fit)

        # Dont change output/return
        return (T, re)