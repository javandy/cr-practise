import time
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
a = '炮车'
#img = Image.open("resource/"+a+".jpg")
#img = Image.open("resource/三枪.jpg")
#new_img = img.resize((135, 160), Image.BILINEAR)
#new_img.save(a+".jpg")
#new_img.show()
im=mpimg.imread('resource/' + a + '.jpg')
# plt.ion()
# im = Image.open('resource/'+ out[index] + '.jpg')
plt.imshow(im)
plt.show()
#time.sleep(1)
plt.close()
