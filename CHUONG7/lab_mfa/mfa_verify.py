import pyotp 
 
# 1. Đọc secret key từ file
secret = ""
totp = pyotp.TOTP(secret) 
 
# 2. Bước 1: Nhập mật khẩu 
password = input("Nhập mật khẩu: ") 
if password != "123456": 
    print(" Mật khẩu sai!") 
    exit() 
 
# 3. Bước 2: Nhập mã OTP 
otp = input("Nhập mã OTP từ Google Authenticator: ") 
if totp.verify(otp): 
    print(" Xác thực thành công! Bạn đã đăng nhập.") 
else: 
    print(" Mã OTP sai hoặc hết hạn.")