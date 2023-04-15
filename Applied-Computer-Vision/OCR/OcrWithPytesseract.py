from PIL import Image
import pytesseract
import pandas as pd
import numpy as np

image = Image.open("---------png------- path file")
width, height = image.size
    
    
df = pytesseract.image_to_data(image, output_type='data.frame')
cols = df.select_dtypes('float').columns
print(df)