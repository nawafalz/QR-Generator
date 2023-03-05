import pyqrcode


my_gitHub_URL = 'https://github.com/nawafalz'

img = pyqrcode.create(my_gitHub_URL).png('my_QR.png',scale=24,background=[150,0,0,150],quiet_zone=1,module_color=[50,50,1,255])


