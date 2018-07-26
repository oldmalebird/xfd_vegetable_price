#汇总全国价格
import pandas as pd
#python D:\Github\xfd_vegetable_price\汇总全国价格.py
docList = ["批发价格 18.1.10.xls",
"批发价格 18.1.20.xls",
"批发价格 18.1.31.xls",
"批发价格 18.2.10.xls",
"批发价格 18.2.20.xls",
"批发价格 18.2.28.xls",
"批发价格 18.3.10.xls",
"批发价格 18.3.20.xls",
"批发价格 18.3.31.xls",
"批发价格 18.4.10.xls",
"批发价格 18.4.20.xls",
"批发价格 18.4.30.xls",
"批发价格 18.5.10.xls",
"批发价格 18.5.20.xls",
"批发价格 18.5.31.xls",
"批发价格 18.6.10.xls",
"批发价格 18.6.20.xls",
"批发价格 18.6.30.xls"
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
df = pd.read_excel(r'D:\Data\新发地菜价\普通菜\新发地每日蔬菜价格表-20160803.xls', sheet_name='Sheet1', header = 1, skipfooter = 3, parse_cols = 'A:F')
#print(df.describe())
df['日期'] = '2016-08-03'
print(df.head())
#print(df.describe())
print(df.tail())
#提取其他文件


for i in range(1, len(commonVegList)):
    print('i=', i)
    docName = commonVegList[i]
    doc_address = r'D:\Data\新发地菜价\普通菜'
    doc_address += '\\' + docName
    print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(doc_address, sheet_name='Sheet1', header = 1, skipfooter = 3, parse_cols = 'A:F')
    #print(df_temp.head())
    colDate = str(docName[11:15]) + '-' + str(docName[15:17]) + '-' + str(docName[17:19])
    print('本次添加的colDate为：', colDate)
    #print(type(colDate))
    df_temp['日期'] = colDate
    df = df.append(df_temp)
    #print(df.tail())
    i += 1

print(df.tail())


writer = r'D:\Data\新发地菜价\普通菜\普通菜价格汇总.xlsx'
df.to_excel(writer, sheet_name='普通菜价格汇总')

#python D:\Github\xfd_vegetable_price\汇总全国价格.py
