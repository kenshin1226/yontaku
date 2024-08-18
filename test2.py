rows=[(1, 'Alice', 30, 'password', '女'), (2, 'Bob', 25, 'hello', '男'), (3, 'taro', 20, 'あいうえお', '男'), (4, 'jiro', 15, '12345', '男'), (5, 'ken', 17, 'abcde', '男'), (6, 'aaa', 40, '1357', '女'), (7, 'Alice2', 30, 'alice@', '女')]
name=input("名前を入力してください")
for i in range(7):
    if name in rows[i]:
        print("YES")
        password=input("passwordを入力してください")
        if rows[i][3]==password:
            print("合格")
    else:
        print("NO") 