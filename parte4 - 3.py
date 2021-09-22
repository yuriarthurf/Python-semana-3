import numpy as np
from matplotlib import pyplot as plt
from PIL import Image, ImageOps

#1
image = np.array(Image.open('python_image.jpg'))
plt.imshow(image)
plt.axis('off')
plt.show()
plt.savefig('imagem_python.png')

#2
image2 = np.fliplr(image)
plt.imshow(image2)
plt.savefig('python_horizontal.png')
plt.show()

#3
image3 = np.flipud(image)
plt.imshow(image3)
plt.savefig('python_vertical.png')
plt.show()

#4
image4 = np.rot90(image, k=1, axes=(0, 1))
plt.imshow(image4)
plt.savefig('python_90_graus.png')
plt.show()
#
# print('Shape da imagem: {}, dtype: {}'.format(image.shape, image.dtype))