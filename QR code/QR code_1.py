import qrcode as qr
img = qr.make("Enter your phone number here or any thing you want to encode in the QR code")
img.save("Phone_Number.png")