import cv2
import csv
import os
import numpy as np
from sklearn.cluster import KMeans
from Get_data import DataLoading
import matplotlib.pyplot as plt


class ColorPaletteGeneration:
    def __init__(self,img_path,n_colors=6):
        self.data=DataLoading(img_path)
        self.kmeans= KMeans(n_clusters=n_colors, random_state=42)
        self.colors_lab=None
        self.rgb_palette=None
        self.save_folder="assets"
        os.makedirs(self.save_folder, exist_ok=True)
        self.save_path = os.path.join(self.save_folder, "palette.png")

    def fittingData(self):
        self.data.readImg()
        self.data.flattenImg()
        self.kmeans.fit(self.data.pixels_lab)
        self.colors_lab=self.kmeans.cluster_centers_.astype(np.uint8)

    def plotAndSaveColors(self):
        if self.colors_lab is None:
            raise ValueError("Run fittingData() first.")
        
        colors_lab_img = self.colors_lab.reshape(-1, 1, 3)
        self.rgb_palette = cv2.cvtColor(colors_lab_img, cv2.COLOR_LAB2RGB).reshape(-1, 3)
        
        plt.figure(figsize=(6, 2))
        plt.axis("off")
        plt.imshow([self.rgb_palette])
        plt.savefig(self.save_path, bbox_inches='tight')  # Save to file
        plt.close()

  

    
       