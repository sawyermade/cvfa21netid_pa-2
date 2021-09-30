##### IMPORTS START #####
import imageio, sys, os, numpy as np, zipfile, math
from tqdm import tqdm
from skimage.transform import warp
from skimage.transform import resize
import cv2
import urllib.request
import matplotlib.pyplot as plt
sift_testing_blah = cv2.SIFT_create(nOctaveLayers = 3, contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6)
##### IMPORTS END #####



##### COLAB STUFF START #####
# Check if using Colab, do not change
try:
    # Mount google drive
    from google.colab import drive
    # drive_dir = '/content/drive'
    # drive.mount(drive_dir)

    # Download image data
    data_dir_parent = '/content'
    data_dir = os.path.join(data_dir_parent, 'data')
    data_zip = '/content/data.zip'
    url = 'https://danielsawyer.com/pa_2_data.zip'

    # If data isnt already downloaded, downloads it and extracts
    if not os.path.exists(data_dir):
        urllib.request.urlretrieve(url, data_zip)

        # Extract image data
        with zipfile.ZipFile(data_zip, 'r') as zf:
            zf.extractall(data_dir_parent)
            print(f'\nlist of {data_dir} directory: {os.listdir(data_dir)}\n')

    # Set colab flag
    COLAB = True

except Exception as e:
    COLAB = False
    data_dir = None
##### COLAB STUFF END #####



##### HELPERS START #####
# Gets paths to images in data directory
def get_image_paths(data_dir):
    # Pull image files in dir, must be png, jpg, jpeg
    img_exts = ['png', 'jpg', 'jpeg']
    img_list = os.listdir(data_dir)
    img_list = [f for f in img_list if f.rsplit('.', 1)[-1] in img_exts]

    # Check to make sure it found images, exit if not
    if not img_list:
        print(f'No images found in {data_dir}. Exiting program...\n') 
        sys.exit(1)

    # Add directory to path of image files
    img_path_list = [os.path.join(data_dir, f) for f in img_list]
    img_path_list = [f for f in img_path_list if os.path.isfile(f)]
    img_path_list.sort()

    # Check to make sure it found image paths, exit if not
    if not img_path_list:
        print(f'No images found in {data_dir}. Exiting program...\n')
        sys.exit(1)

    return img_path_list
##### HELPERS END #####



def main():
    # Args, checks if colab or not
    if COLAB:
        global data_dir
        global estimate_transforms
    else:
        # Import estimate_transforms class from est_trans.py
        from est_trans import estimate_transforms

        # Download image data
        data_dir_parent = './'
        data_dir = os.path.join(data_dir_parent, 'data')
        data_zip = os.path.join(data_dir_parent, 'data.zip')
        url = 'https://danielsawyer.com/pa_2_data.zip'

        # If data isnt already downloaded, downloads it and extracts
        if not os.path.exists(data_dir):
            urllib.request.urlretrieve(url, data_zip)

            # Extract image data
            with zipfile.ZipFile(data_zip, 'r') as zf:
                zf.extractall(data_dir_parent)
                print(f'list of {data_dir} directory: {os.listdir(data_dir)}\n')

    # Make sure data directory exists
    if not os.path.exists(data_dir):
        print(f'data_dir: {data_dir} does not exist. Exiting program...\n')
        sys.exit(1)

    # Get full paths for images in data directory
    img_path_list = get_image_paths(data_dir)

    # Run fitting
    for i in range(0, len(img_path_list), 2):
        # Get regular image path
        img_path_reg = img_path_list[i]

        # Get warped image path
        img_path_warped = img_path_list[i+1]

        # Load them into the class
        est = estimate_transforms(img_path_reg, img_path_warped)
        
        # Run fitting
        T_aff, re_aff = est.fit_affine()
        T_rt, re_rt = est.fit_rotate_translation()
        T_per, re_per = est.fit_perspective()

        # Compare & choose the best one, you figure this out
        #CODE HERE


if __name__ == '__main__':
    main()