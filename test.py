import chardet
print(chardet.detect(b'Hello, world!')['encoding'])
# print(chardet.detect(b'价格不错 大黄瓜种植户却很受伤.txt')['encoding'])
# print(chardet.detect(b'市场）元宵后蔬菜市场：量足价跌 交易​繁忙.txt')['encoding'])
a = "D:/Data/小程序/北方蔬菜报/2017/20170106/北方蔬菜报2017.01.06/1热点关注/数九隆冬 葡萄飘香.txt"
b = "D:/Data/小程序/北方蔬菜报/2017/20170811/2017.8.11/170811黄瓜死棵重? 区别来防治.txt"
print(type(a))
f = open(a)
print(f.read())
#print(chardet.detect(f.read())['encoding'])
# f = open(b)
# print(f.read())
# print(chardet.detect(f.read())['encoding'])

# f = open(
#     "D:\\Data\\小程序\\北方蔬菜报\\2017\\20170217\\北方蔬菜报2017.02.17\\市场\\市场）元宵后蔬菜市场：量足价跌 交易繁忙.txt"
# )

# address = "D:\Data\小程序\北方蔬菜报\2017\20170217\北方蔬菜报2017.02.17\市场\市场）元宵后蔬菜市场：量足价跌 交易​繁忙.txt"
# start = 'r"'
# end = '"'
# f = open(start + address + end, 'rb')
# print(chardet.detect(f.read())['encoding'])
