#提取
import pandas as pd
#python D:\Github\xfd_vegetable_price\specialVegCollect.py
specialVegList = [
    '新发地特菜价格表-20180726.xls', '新发地特菜价格表-20180801.xls', '新发地特菜价格表-20180807.xls',
    '新发地特菜价格表-20180811.xls', '新发地特菜价格表-20180815.xls', '新发地特菜价格表-20180822.xls',
    '新发地特菜价格表-20180905.xls', '新发地特菜价格表-20180912.xls', '新发地特菜价格表-20180921.xls',
    '新发地特菜价格表-20180926.xls', '新发地特菜价格表-20181001.xls', '新发地特菜价格表-20181006.xls',
    '新发地特菜价格表-20181011.xls', '新发地特菜价格表-20181016.xls', '新发地特菜价格表-20181020.xls',
    '新发地特菜价格表-20181025.xls', '新发地特菜价格表-20181031.xls', '新发地特菜价格表-20181106.xls',
    '新发地特菜价格表-20181110.xls', '新发地特菜价格表-20181116.xls', '新发地特菜价格表-20181121.xls',
    '新发地特菜价格表-20181201.xls'
]

df = pd.read_excel(
    r"C:\Users\cva_b\Desktop\菜价\特菜\新发地特菜价格表-20180726.xls",
    sheet_name='Sheet1',
    header=None,
    names=["品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万吨）", "交易额（万元）"],
    skiprows=3,
    skipfooter=4,
    usecols='A:F')
#print(df.describe())
df['日期'] = '2018-07-26'
#print(df.head())
#print(df)
#print(df.describe())
print(df.head())

for i in range(1, len(specialVegList)):
    docName = specialVegList[i]
    doc_address = r'C:\Users\cva_b\Desktop\菜价\特菜'
    doc_address += '\\' + docName
    #print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(
        doc_address,
        sheet_name='Sheet1',
        header=None,
        names=["品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万吨）", "交易额（万元）"],
        skiprows=3,
        skipfooter=4,
        use_cols='A:F')
    #print(df_temp.head())
    colDate = str(docName[9:13]) + '-' + str(docName[13:15]) + '-' + str(
        docName[15:17])
    #print('本次添加的colDate为：', colDate)
    #print(type(colDate))
    df_temp['日期'] = colDate
    df = df.append(df_temp)
    i += 1

print(df.tail())
writer = r'D:\Data\新发地菜价\特菜\特菜价格汇总20180723-1206.xls'
df.to_excel(writer, sheet_name='特菜价格汇总', index=False)

#python D:\Github\xfd_vegetable_price\specialVegCollect.py
