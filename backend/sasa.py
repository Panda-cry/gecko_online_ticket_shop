import datetime

import pyotp
import qrcode

key = pyotp.random_base32(32)

uri = pyotp.TOTP(key).provisioning_uri(name="Pera Peric",
                                       issuer_name="Online store app")
print(uri)

qrcode.make(uri).save("totp.png")


totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter code :")))