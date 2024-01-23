import segno

#create new QR to a website
qrcode = segno.make_qr("alecandalli.com")

#Save QR to a png
qrcode.save(
    "wide_border_qrcode.png",
    scale=15,
    border=1,
)