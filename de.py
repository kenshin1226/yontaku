import sqlite3
# データベースに接続（ファイルが存在しない場合は自動的に作成されます）
conn = sqlite3.connect('yontakudatabase.db')
cursor = conn.cursor()

# データを一括で更新
# users_seibetu = [
#     (1, '女'),
#     (2, '男'),
#     (3, '男'),
#     (4, '男'),
#     (5, '男'),
#     (6, '女'),
# ]
sql="INSERT INTO users (name, age, pass,seibetu) VALUES(?,?,?,?) "
cursor.execute(sql,('Alice2', 30, 'alice@','女'))

# for user_id, seibetu in users_seibetu:
#     cursor.execute("UPDATE users SET seibetu = ? WHERE id = ?", (seibetu, user_id))

# 変更を保存
conn.commit()

# データを確認
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# 接続を閉じる
conn.close()
