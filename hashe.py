import bcrypt

# パスワードのハッシュ化
password = b"abc"  # パスワードはバイト文字列にする必要があります
hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

print(f"Hashed password: {hashed_password}")

# ハッシュ化されたパスワードと入力されたパスワードを比較して検証
entered_password = b"abcde"
if bcrypt.checkpw(entered_password, hashed_password):
    print("Password is correct!")
else:
    print("Password is incorrect.")
