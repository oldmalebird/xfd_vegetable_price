for line in open("D:\specialVegList.txt", 'r'):  # 打开文件
    a = line.replace('\n', '')  # 替换换行符
    print(a)  # 显示替换后的行

for line in open("D:\waterVegList.txt", 'r'):  # 打开文件
    b = line.replace('\n', '')  # 替换换行符
    print(b)  # 显示替换后的行

for line in open("D:\commonVegList.txt", 'r'):  # 打开文件
    c = line.replace('\n', '')  # 替换换行符
    print(c)  # 显示替换后的行
