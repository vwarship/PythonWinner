"""二值化降噪的过程"""

from PIL import Image,ImageEnhance,ImageFilter


im = Image.open("images/idcode1.jpeg")
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.show()
