import cv2 as cv

def image_rgb_to_gray(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return img_gray
