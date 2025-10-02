import cv2
import csv 
import os

class DataLoading :
    def __init__(self,image_path):
        self.image_path=image_path
        self.img=None
        self.pixels_lab=None
    
    def readImg(self):
        self.img=cv2.imread(self.image_path)
        if self.img is None:
            raise FileNotFoundError(f"Image not found at {self.image_path}")
        self.img=cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)
    
    def flattenImg(self):
        if self.img is None:
            raise ValueError("Image not loaded. Call readImg() first.")
        
        img_lab=cv2.cvtColor(self.img,cv2.COLOR_RGB2LAB)
        self.pixels_lab=img_lab.reshape(-1,3)
        
       
    