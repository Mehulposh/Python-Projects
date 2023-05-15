import pyqrcode
import png
from pyqrcode import QRCode

# Text which is to be converted to QR code
#print("Enter text to convert")
#s = input(""": """)
a = """Mehul Poshattiwar
    7218470664
    mehulposhattiwar4995@gmail.com
    https://github.com/Mehulposh/Mycodes.git """
# Name of QR code png file
print("Enter image name to save")
n = input(": ")
# Adding extension as .pnf
d = n + ".png"
# Creating QR code
url = pyqrcode.create(a)
# Saving QR code as  a png file
url.show()
url.png(d, scale=6)