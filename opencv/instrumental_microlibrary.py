#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on December 14, 2016 by 5:25 PM

import numpy as np
import cv2
import matplotlib.pyplot as plt


class ImageProcMicroLibrary():
    def __init__(self,image_name):
        self.image = cv2.imread(image_name)
        self.rows,self.cols,self.channels = self.image.shape

    def GetImgeSize(self):
        return "The image is {0} x {1} and has {2} channels".format(self.rows,self.cols, self.channels)

    def __WeightedAverage(self,pixel):
        return 0.299*pixel[0] + 0.587*pixel[1] + 0.114*pixel[2]

    def __SimpleAverage(self,pixel):
        return (pixel[0] + pixel[1] + pixel[2]) / 3

    def __WeightedGrayImageConversion(self):
        grey_weighted = np.zeros((self.rows, self.cols),dtype=np.uint8)
        for rownum in range(len(self.image)):
           for colnum in range(len(self.image[rownum])):
              grey_weighted[rownum][colnum] = self.__WeightedAverage(self.image[rownum][colnum])
        return grey_weighted

    def __SimpleGrayImageConversion(self):
        grey_simple = np.zeros((self.rows, self.cols),dtype=np.uint8)
        for rownum in range(len(self.image)):
            for colnum in range(len(self.image[rownum])):
                grey_simple[rownum][colnum] = self.__SimpleAverage(self.image[rownum][colnum])
        return grey_simple

    def __OptimizedGrayImageConversion(self):
        grey_optimized = np.dot(self.image[..., :3], [0.299, 0.587, 0.114])
        return grey_optimized

    def __CropImage(self,x,y,w,h):
        assert x <= self.cols and y<= self.rows and x+w <= self.cols and y+h <= self.rows,\
            "You've chosen a value beyond the dimensions of the image. {}".format(self.GetImgeSize())
        return self.image[y: y + h, x: x + w]

    def ShowOriginalImage(self):
        cv2.imshow("Original Image", self.image)

    def ShowGrayWeightedImage(self, save=False):
        cv2.imshow('Weighted Grey Image',self.__WeightedGrayImageConversion())
        if save == True:
            cv2.imwrite('Weighted_Gray_Image.jpg',self.__WeightedGrayImageConversion())
        else:
            pass

    def ShowGrayAverageImage(self,save=False):
        cv2.imshow('Simple Grey Image', self.__SimpleGrayImageConversion())
        if save == True:
            cv2.imwrite('Simple_Gray_Image.jpg', self.__SimpleGrayImageConversion())
        else:
            pass

    def ShowCroppedImage(self,x,y,w,h, save=False):
        cv2.imshow("Cropped Image", self.__CropImage(x,y,w,h))
        if save==True:
            cv2.imwrite("Cropped_Image.jpg",self.__CropImage(x,y,w,h))
        else:
            pass

    def ShowOptimizedGrayImage(self,save=True):
        plt.imshow(self.__OptimizedGrayImageConversion(), cmap=plt.get_cmap('gray'))
        if save==True:
            plt.savefig('OptimizedGrayImage.jpg')
        else:
            pass
        plt.show()

if __name__ == '__main__':

    img = ImageProcMicroLibrary('ronaldo_messi_chat.jpg')
    img.GetImgeSize()
    img.ShowOriginalImage()
    img.ShowOriginalImage()
    print ''' Image plotting \n
    Keymap :\n
    a - show image in grayscale with simple averaging \n
    b - show image in grayscale with weighted averaging \n
    c - show cropped image \n
    Esc - exit \n
    '''
    while True:
        k = cv2.waitKey(0)&0xFF
        if k == ord('a'):
            print 'a\n This is slow'
            img.ShowGrayAverageImage()
        elif k == ord('b'):
            print 'b\n This is slow too'
            img.ShowGrayWeightedImage(True)
        elif k == ord('c'):
            img.ShowCroppedImage(100, 50, 800, 300)
        elif k == 27:
            print 'ESC'
            cv2.destroyAllWindows()
            break
    cv2.destroyAllWindows()

    img.ShowOptimizedGrayImage()
