# QR Code
import qrcode

from pyzbar.pyzbar import decode
from PIL import Image

import qrcode

myqr = qrcode.make("www.youtube.com/@Morscode77")
myqr.save("myqr.png")

ima = decode(Image.open("myqr.png"))
print(ima[0].data.decode("ascii"))
