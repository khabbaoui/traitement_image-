import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import os


def conversion_en_gris(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def segmentation_par_contour_Canny(image):
    gray = conversion_en_gris(image)
    contour = cv2.Canny(gray, 100, 200)
    return contour


def segmenttation_par_contour_Sobel(image):
    gray = conversion_en_gris(image)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    sobel_magnitude = np.sqrt(sobel_x ** 2 + sobel_y ** 2)
    sobel_magnitude = cv2.normalize(sobel_magnitude, None, 0, 255, cv2.NORM_MINMAX)
    sobel_magnitude = np.uint8(sobel_magnitude)
    return sobel_magnitude


def segment_by_region_thresholding_fixe(image):
    gray = conversion_en_gris(image)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    return thresh


def segment_by_region_thresholding_adaptatif(image):
    gray = conversion_en_gris(image)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh


def process_image(image, method):
    image_path = default_storage.save('tmp/' + image.name, ContentFile(image.read()))
    image_cv = cv2.imread(image_path)

    if method == 'canny':
        processed_image = segmentation_par_contour_Canny(image_cv)
    elif method == 'sobel':
        processed_image = segmenttation_par_contour_Sobel(image_cv)
    elif method == 'threshold_fixe':
        processed_image = segment_by_region_thresholding_fixe(image_cv)
    elif method == 'threshold_adaptatif':
        processed_image = segment_by_region_thresholding_adaptatif(image_cv)

    result_dir = os.path.join('media', 'processed')
    os.makedirs(result_dir, exist_ok=True)
    result_path = os.path.join(result_dir, image.name)
    cv2.imwrite(result_path, processed_image)

    # Print the result path for debugging
    print(f"Processed image saved to: {result_path}")

    return result_path
