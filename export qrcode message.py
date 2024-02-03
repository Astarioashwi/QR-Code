from pyzbar.pyzbar import decode 
from PIL import Image

img = Image.open('C:/Users/akulanga/Pictures/myqrcode1.png')

result = decode(img)

print(result)