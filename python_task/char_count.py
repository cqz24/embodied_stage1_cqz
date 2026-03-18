text = input("请输入一段字符串：")
count = {}
for ch in text:
    count[ch] = count.get(ch,0)+1
print("各字符出现的次数：")
for ch,cnt in count.items():
    print(f"'{ch}' : {cnt}")