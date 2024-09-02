import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity as ssim


def find_difference(image1, image2):
    assert image1.shape == image2.shape, "Images must have same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, diff) = ssim(gray_image1, gray_image2, full=True)
    print(f"SSIM: {score:.2f}")

    return (diff - np.min(diff)) / (np.max(diff) - np.min(diff))


def transform_image(image1, image2):
    return match_histograms(image1, image2, multichannel=True)
