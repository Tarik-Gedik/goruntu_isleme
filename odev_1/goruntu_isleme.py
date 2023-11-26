import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image):
   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    
    histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

    
    plt.plot(histogram)
    plt.title('Gri Tonlama Histogram')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Sıklık')
    plt.show()


image_path = ("odev_1\His.image.jpg") 
image = cv2.imread(image_path)


plot_histogram(image)
