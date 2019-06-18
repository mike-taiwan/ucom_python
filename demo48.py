from PIL import Image
from urllib2 import urlopen

url1 = 'https://www.cwb.gov.tw/Data/radar/CV1_3600_201906181550.png'

fileToSave = urlopen(url1)
image1 = Image.open(fileToSave)
image1.save('images\\orig.png')

half = (image1.size[0] / 2, image1.size[1] / 2)
half_image1 = image1.resize(half, Image.ANTIALIAS)
half_image1.save('images\\small.png')
rot1 = image1.transpose(Image.ROTATE_90)
rot1.save('images\\rot1.png')
rot2 = image1.transpose(Image.ROTATE_180)
rot2.save('images\\rot2.png')
rot3 = image1.transpose(Image.ROTATE_270)
rot3.save('images\\rot3.png')
rot4 = image1.rotate(45)
rot4.save('images\\rot4.png')