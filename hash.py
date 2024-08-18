import hashlib

# ハッシュ化したい文字列
text = "A"

# SHA-256ハッシュオブジェクトを作成
hash_object = hashlib.sha256()

# 文字列をバイト形式に変換してハッシュオブジェクトに渡す
hash_object.update(text.encode('utf-8'))

# ハッシュ値を取得（16進数で表示）
hash_hex = hash_object.hexdigest()

# 結果を表示
print(f"Original Text: {text}")
print(f"SHA-256 Hash: {hash_hex}")
