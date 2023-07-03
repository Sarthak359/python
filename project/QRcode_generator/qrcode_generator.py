import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://www.youtube.com/watch?v=RsN0aXfPR1E")
qr.make(fit=True)
img = qr.make_image(fill_color="blue", back_color="black")
img.save("qr3.png")
