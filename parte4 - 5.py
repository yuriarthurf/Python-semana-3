import numpy as np
from PIL import Image
from matplotlib import pyplot as plt, patches
import PIL.ImageDraw as ImageDraw
import PIL.Image as Image

image = np.array(Image.open('leao.png'))
print('Shape da imagem: {}, dtype: {}'.format(image.shape, image.dtype))
bbox = [67, 80, 175, 187] # x1, y1, x2, y2
print('Coordenadas do bouding box: x1={}, y1={}, x2={}, y2={}'.format(*bbox))


image[0:67,:,2] = 0
image[0:67,:,1] = 0
image[0:67,:,0] = 0
image[:,0:80,2] = 0
image[:,0:80,1] = 0
image[:,0:80,0] = 0
image[175:568,:,2] = 0
image[175:568,:,1] = 0
image[175:568,:,0] = 0
image[:, 187:945,2] = 0
image[:, 187:945,1] = 0
image[:, 187:945,0] = 0

plt.imshow(image)
plt.show()

# fig, ax = plt.subplots()
# ax.imshow(image)
# rect = patches.Rectangle((67,80), 175,187, color='blue', fill=None, linewidth=2)
# rect2 = patches.Rectangle((0,0), 945, 67, color='black', fill=True, linewidth=10)
# rect3 = patches.Rectangle((258, 90), 945, 568, color='black', fill=True, linewidth=10)
# rect4 = patches.Rectangle((0, 280), 945, 568, color='black', fill=True, linewidth=10)
# rect5 = patches.Rectangle((0, 90), 50, 260, color='black', fill=True, linewidth=10)
# ax.add_patch(rect)
# ax.add_patch(rect2)
# ax.add_patch(rect3)
# ax.add_patch(rect4)
# ax.add_patch(rect5)

# plt.imshow(image)
# plt.show()

