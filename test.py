abc={"a":"1",
     "b":"2",
     "c":"3",
     "z":"26"}
print(abc["b"])
if "z" in abc:
    print(abc["z"])
p=input("文字を記入してください")
if p in abc:
    print("あった")
    passw=input("passwordを記入してください")
    if abc[p]==passw:
        print("合格")
    else:
        print("不合格")
else:
    print("ない")