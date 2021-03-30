
# Import packages
import os
from PIL import Image
import pandas as pd

# Descriptive statistics of current image sizes
width = []
height = []

for i in range(1,56):
    img = Image.open('raw_images/image' + str(i) + '.jpg')
    im_width=img.size[0]
    im_height=img.size[1]
    width.append(im_width)
    height.append(im_height)


estat_dim = {
    "dim" : ["width","height"],
    "mean" : [int(sum(width)/len(width)),int(sum(height)/len(height))],
    "min" : [min(width),min(height)],
    "max" : [max(width),max(height)]
}

estat_dim=pd.DataFrame(estat_dim)
estat_dim

#create images file
os.makedirs("images", exist_ok=True)

#Resize each image
for i in range(1,56):
    img = Image.open('raw_images/image' + str(i) + '.jpg')
    wpercent = (estat_dim["mean"][0] / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((estat_dim["mean"][0], hsize), Image.ANTIALIAS)
    img.save('images/resize_image' + str(i) + '.jpg')
print('Successfully images resized')

# Descriptive statistics of resized images

width = []
height = []

for i in range(1,56):
    img = Image.open('images/resize_image' + str(i) + '.jpg')
    im_width=img.size[0]
    im_height=img.size[1]
    width.append(im_width)
    height.append(im_height)
    
estat_dim = {
    "dim" : ["width","height"],
    "mean" : [int(sum(width)/len(width)),int(sum(height)/len(height))],
    "min" : [min(width),min(height)],
    "max" : [max(width),max(height)]
}

estat_dim=pd.DataFrame(estat_dim)
estat_dim