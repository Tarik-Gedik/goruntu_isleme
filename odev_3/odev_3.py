import cv2
import numpy as np

image = cv2.imread('pirinc_resmi.jpg',C:\Users\t_g-2\Desktop\odev_3)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=30)

contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

rice_grain_count = len(contours)
print(f"Pirinç tanesi sayısı: {rice_grain_count}")

result = image_rgb.copy()
cv2.drawContours(result, contours, -1, (0, 255, 0), 2)

cv2.imshow('Thresholding Uygulanmış Resim', thresh)
cv2.imshow('Konturlar', result)
cv2.waitKey(0)
cv2.destroyAllWindows()