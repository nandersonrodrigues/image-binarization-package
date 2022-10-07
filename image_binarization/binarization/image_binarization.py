import cv2 as cv

def apply_blurr(img_gray):
    img_blur = cv.medianBlur(img_gray, 5)
    return img_blur

def apply_binarization_gaussian(img_blur):
    img_thresholding = cv.adaptiveThreshold(img_blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV,7,2)
    return img_thresholding

def apply_binarization_mean(img_blur):
    img_thresholding = cv.adaptiveThreshold(img_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV,5,2)
