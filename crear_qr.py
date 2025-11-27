import qrcode

# 🔴 IMPORTANTE: Cambia esto por la IP de tu computadora
url = "https://vanessasalcedo.pythonanywhere.com/"

# Generar QR
img = qrcode.make(url)
img.save("qr_hazlo_tu_mismo.png")

print("QR generado: qr_hazlo_tu_mismo.png")
