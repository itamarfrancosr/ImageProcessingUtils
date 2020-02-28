import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('spdata_vuelo1.csv')

BBox = (df.Longitude.min(), df.Longitude.max(), df.Latitude.min(), df.Latitude.max())

# inia_map = plt.imread('map5.png')


fig, ax = plt.subplots(figsize=(8, 7))

ax.scatter(df.Longitude, df.Latitude, zorder=1, alpha= 0.8, c='r', s=10)
for i in range(len(df)):
    ax.annotate(df.Filename[i], (df.Longitude[i], df.Latitude[i]))

ax.set_title('Plotting Spatial Data on INIA Map')
ax.set_xlim(BBox[0], BBox[1])
ax.set_ylim(BBox[2], BBox[3])
#ax.imshow(inia_map, zorder=0, extent=BBox, aspect='equal')
plt.show()



# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from skimage.transform import resize
# import pandas as pd
#
# def getImage(path):
#     image = plt.imread(path)
#     image_resized = resize(image, (image.shape[0] // 500, image.shape[1] // 500),
#                            anti_aliasing=True)
#     return OffsetImage(image_resized)
#
# paths = [
#     'av1.jpg',
#     'av1.jpg',
#     'av1.jpg',
#     'av1.jpg',
#     'av1.jpg']
#
# x = [0, 1, 2, 3, 4]
# y = [0, 1, 2, 3, 4]
#
# fig, ax = plt.subplots()
# ax.scatter(x, y)
#
# for x0, y0, path in zip(x, y,paths):
#     ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
#     ax.add_artist(ab)
# plt.show()


# import os
# import glob
# import matplotlib.pyplot as plt
# from matplotlib.offsetbox import OffsetImage, AnnotationBbox
# from skimage.transform import resize
# import pandas as pd
#
# def getImage(path):
#     image = plt.imread(path)
#     image_resized = resize(image, (image.shape[0] // 500, image.shape[1] // 500))
#     return OffsetImage(image_resized)
#
#
# df = pd.read_csv('spdata01_aux.csv')
#
# img_dir = 'E:/AvocadoTrees/DJI/13-02-2020/vuelo1/imagenes2/'
# data_path = os.path.join(img_dir,'*g')
# files = glob.glob(data_path)
#
# fig, ax = plt.subplots()
# ax.scatter(df.Longitude, df.Latitude, zorder=1, alpha= 0.8, c='r', s=1)
#
# counter = 0
# for x0, y0, f1 in zip(df['Latitude'], df['Longitude'], files):
#     ab = AnnotationBbox(getImage(f1), (x0, y0), frameon=False)
#     ax.add_artist(ab)
#     print(counter)
#     counter += 1
#
# plt.show()





