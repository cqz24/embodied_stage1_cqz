filename = input("请输入要统计的文件名(如 text.txt):")
try:
    with open(filename,'r',encoding='utf-8')as f:
        lines = 0
        words = 0
        for line in f:
            lines +=1
            words += len(line.split())
    print(f"文件{filename}统计结果: ")
    print(f"行数:{lines}")
    print(f"单词数：{words}")
except FileNotFoundError:
    print("文件不存在，请检查文件名！")