import pyotp 
import qrcode 
# 1. Sinh secret key 
secret = pyotp.random_base32() 
print("SECRET:", secret) 
# 2. Ghi secret ra file để dùng lại 
with open("secret.txt", "w") as f: 
    f.write(secret) 
# 3. Tạo URI chuẩn otpauth 
totp = pyotp.TOTP(secret) 
uri = totp.provisioning_uri(name="luongducthang289@gmail.com", 
issuer_name="MyMFAApp")

# 4. Tạo mã QR để quét 
img = qrcode.make(uri) 
img.save("F:\\mạng máy tính và truyền dữ liệu\\chương 7\\lab_mfaotp_qr_ver1.png") 
print("Đã tạo mã QR trong file 'otp_qr.png')") 