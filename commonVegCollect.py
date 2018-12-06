import pandas as pd
commonVegList = [
    '新发地每日蔬菜价格表-20180723.xls', '新发地每日蔬菜价格表-20180724.xls',
    '新发地每日蔬菜价格表-20180725.xls', '新发地每日蔬菜价格表-20180726.xls',
    '新发地每日蔬菜价格表-20180727.xls', '新发地每日蔬菜价格表-20180728.xls',
    '新发地每日蔬菜价格表-20180729.xls', '新发地每日蔬菜价格表-20180730.xls',
    '新发地每日蔬菜价格表-20180731.xls', '新发地每日蔬菜价格表-20180801.xls',
    '新发地每日蔬菜价格表-20180802.xls', '新发地每日蔬菜价格表-20180803.xls',
    '新发地每日蔬菜价格表-20180804.xls', '新发地每日蔬菜价格表-20180805.xls',
    '新发地每日蔬菜价格表-20180806.xls', '新发地每日蔬菜价格表-20180807.xls',
    '新发地每日蔬菜价格表-20180808.xls', '新发地每日蔬菜价格表-20180809.xls',
    '新发地每日蔬菜价格表-20180810.xls', '新发地每日蔬菜价格表-20180811.xls',
    '新发地每日蔬菜价格表-20180812.xls', '新发地每日蔬菜价格表-20180813.xls',
    '新发地每日蔬菜价格表-20180814.xls', '新发地每日蔬菜价格表-20180815.xls',
    '新发地每日蔬菜价格表-20180816.xls', '新发地每日蔬菜价格表-20180817.xls',
    '新发地每日蔬菜价格表-20180818.xls', '新发地每日蔬菜价格表-20180819.xls',
    '新发地每日蔬菜价格表-20180820.xls', '新发地每日蔬菜价格表-20180821.xls',
    '新发地每日蔬菜价格表-20180822.xls', '新发地每日蔬菜价格表-20180824.xls',
    '新发地每日蔬菜价格表-20180825.xls', '新发地每日蔬菜价格表-20180826.xls',
    '新发地每日蔬菜价格表-20180827.xls', '新发地每日蔬菜价格表-20180828.xls',
    '新发地每日蔬菜价格表-20180829.xls', '新发地每日蔬菜价格表-20180830.xls',
    '新发地每日蔬菜价格表-20180831.xls', '新发地每日蔬菜价格表-20180901.xls',
    '新发地每日蔬菜价格表-20180902.xls', '新发地每日蔬菜价格表-20180903.xls',
    '新发地每日蔬菜价格表-20180904.xls', '新发地每日蔬菜价格表-20180905.xls',
    '新发地每日蔬菜价格表-20180906.xls', '新发地每日蔬菜价格表-20180907.xls',
    '新发地每日蔬菜价格表-20180908.xls', '新发地每日蔬菜价格表-20180910.xls',
    '新发地每日蔬菜价格表-20180911.xls', '新发地每日蔬菜价格表-20180912.xls',
    '新发地每日蔬菜价格表-20180913.xls', '新发地每日蔬菜价格表-20180914.xls',
    '新发地每日蔬菜价格表-20180915.xls', '新发地每日蔬菜价格表-20180916.xls',
    '新发地每日蔬菜价格表-20180917.xls', '新发地每日蔬菜价格表-20180918.xls',
    '新发地每日蔬菜价格表-20180919.xls', '新发地每日蔬菜价格表-20180920.xls',
    '新发地每日蔬菜价格表-20180921.xls', '新发地每日蔬菜价格表-20180922.xls',
    '新发地每日蔬菜价格表-20180924.xls', '新发地每日蔬菜价格表-20180925.xls',
    '新发地每日蔬菜价格表-20180926.xls', '新发地每日蔬菜价格表-20180927.xls',
    '新发地每日蔬菜价格表-20180928.xls', '新发地每日蔬菜价格表-20180929.xls',
    '新发地每日蔬菜价格表-20180930.xls', '新发地每日蔬菜价格表-20181001.xls',
    '新发地每日蔬菜价格表-20181002.xls', '新发地每日蔬菜价格表-20181003.xls',
    '新发地每日蔬菜价格表-20181004.xls', '新发地每日蔬菜价格表-20181005.xls',
    '新发地每日蔬菜价格表-20181006.xls', '新发地每日蔬菜价格表-20181007.xls',
    '新发地每日蔬菜价格表-20181008.xls', '新发地每日蔬菜价格表-20181009.xls',
    '新发地每日蔬菜价格表-20181010.xls', '新发地每日蔬菜价格表-20181011.xls',
    '新发地每日蔬菜价格表-20181012.xls', '新发地每日蔬菜价格表-20181013.xls',
    '新发地每日蔬菜价格表-20181014.xls', '新发地每日蔬菜价格表-20181015.xls',
    '新发地每日蔬菜价格表-20181016.xls', '新发地每日蔬菜价格表-20181017.xls',
    '新发地每日蔬菜价格表-20181018.xls', '新发地每日蔬菜价格表-20181019.xls',
    '新发地每日蔬菜价格表-20181020.xls', '新发地每日蔬菜价格表-20181021.xls',
    '新发地每日蔬菜价格表-20181022.xls', '新发地每日蔬菜价格表-20181023.xls',
    '新发地每日蔬菜价格表-20181024.xls', '新发地每日蔬菜价格表-20181025.xls',
    '新发地每日蔬菜价格表-20181026.xls', '新发地每日蔬菜价格表-20181027.xls',
    '新发地每日蔬菜价格表-20181028.xls', '新发地每日蔬菜价格表-20181029.xls',
    '新发地每日蔬菜价格表-20181030.xls', '新发地每日蔬菜价格表-20181031.xls',
    '新发地每日蔬菜价格表-20181101.xls', '新发地每日蔬菜价格表-20181102.xls',
    '新发地每日蔬菜价格表-20181103.xls', '新发地每日蔬菜价格表-20181104.xls',
    '新发地每日蔬菜价格表-20181105.xls', '新发地每日蔬菜价格表-20181106.xls',
    '新发地每日蔬菜价格表-20181107.xls', '新发地每日蔬菜价格表-20181108.xls',
    '新发地每日蔬菜价格表-20181109.xls', '新发地每日蔬菜价格表-20181110.xls',
    '新发地每日蔬菜价格表-20181111.xls', '新发地每日蔬菜价格表-20181112.xls',
    '新发地每日蔬菜价格表-20181113.xls', '新发地每日蔬菜价格表-20181114.xls',
    '新发地每日蔬菜价格表-20181115.xls', '新发地每日蔬菜价格表-20181116.xls',
    '新发地每日蔬菜价格表-20181117.xls', '新发地每日蔬菜价格表-20181118.xls',
    '新发地每日蔬菜价格表-20181119.xls', '新发地每日蔬菜价格表-20181120.xls',
    '新发地每日蔬菜价格表-20181121.xls', '新发地每日蔬菜价格表-20181122.xls',
    '新发地每日蔬菜价格表-20181123.xls', '新发地每日蔬菜价格表-20181124.xls',
    '新发地每日蔬菜价格表-20181125.xls', '新发地每日蔬菜价格表-20181126.xls',
    '新发地每日蔬菜价格表-20181127.xls', '新发地每日蔬菜价格表-20181128.xls',
    '新发地每日蔬菜价格表-20181129.xls', '新发地每日蔬菜价格表-20181130.xls',
    '新发地每日蔬菜价格表-20181201.xls', '新发地每日蔬菜价格表-20181203.xls',
    '新发地每日蔬菜价格表-20181204.xls', '新发地每日蔬菜价格表-20181205.xls',
    '新发地每日蔬菜价格表-20181206.xls'
]

#提取第一个文件
'''
parse_cols : int or list, default None
Deprecated since version 0.21.0: Pass in usecols instead.
usecols : int or list, default None
If None then parse all columns,
If int then indicates last column to be parsed
If list of ints then indicates list of column numbers to be parsed
If string then indicates comma separated list of Excel column letters and column ranges (e.g. “A:E” or “A,C,E:F”). Ranges are inclusive of both sides.
'''
df = pd.read_excel(
    r'C:\Users\cva_b\Desktop\菜价\普通菜\新发地每日蔬菜价格表-20180723.xls',
    sheet_name='Sheet1',
    header=None,
    names=["品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万吨）", "交易额（万元）"],
    skiprows=2,
    skipfooter=4,
    usecols='A:F')

#print(df.describe())
df['日期'] = '2018-07-23'
print(df.head())
#print(df.describe())
print(df.tail())
#提取其他文件

for i in range(1, len(commonVegList)):
    print('i=', i)
    docName = commonVegList[i]
    doc_address = r'C:\Users\cva_b\Desktop\菜价\普通菜'
    doc_address += '\\' + docName
    print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(
        doc_address,
        sheet_name='Sheet1',
        header=None,
        names=["品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万吨）", "交易额（万元）"],
        skiprows=2,
        skipfooter=3,
        usecols='A:F')
    #print(df_temp.head())
    colDate = str(docName[11:15]) + '-' + str(docName[15:17]) + '-' + str(
        docName[17:19])
    print('本次添加的colDate为：', colDate)
    #print(type(colDate))
    df_temp['日期'] = colDate
    df = df.append(df_temp)
    #print(df.tail())
    i += 1

print(df.tail())

#后缀名可为xlsx
writer = r'D:\Data\新发地菜价\普通菜\普通菜价格汇总20180723-1206.xls'
df.to_excel(writer, sheet_name='普通菜价格汇总', index=False)

#python D:\Github\xfd_vegetable_price\commonVegCollect.py
