USER_CREDENTIALS = {
    "admin": "password",
    "user1": "mypassword1",
    "user2": "mypassword2",
}
username="sugizaki"
USER_CREDENTIALS[username]="12345"
print(USER_CREDENTIALS)
if username in USER_CREDENTIALS:
    print("OK")
#and USER_CREDENTIALS[username] == password::

#ユーザー名が事前に定義されたユーザー認証情報（USER_CREDENTIALS）の中に存在し、かつ入力されたパスワードがそのユーザー名に対応するパスワードと一致するかどうかを確認します。