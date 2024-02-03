import qrcode

data = 'Hello World.. Get ready to get your QR Codes'

img = qrcode.make(data)

img.save('C:/Users/akulanga/Pictures/myqrcode.png')