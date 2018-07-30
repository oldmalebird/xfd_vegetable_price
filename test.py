#汇总全国价格
import pandas as pd

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

df = pd.read_excel(r'E:\peng\批发价格 18.1.10.xls', sheet_name='Report', header = None, name = ["蔬菜","省","市","批发市场","日期","大宗价","最高价","最低价","交易量","产地"], skiprows = 11,  skipfooter = 3)
#print(df.describe())
#print(df.head())
#print(df.describe())
#print(df.tail())
#提取其他文件

for i in range(1, len(docList)):
    print('i=', i)
    docName = docList[i]
    doc_address = r'E:\peng'
    doc_address += '\\' + docName
    print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(doc_address, sheet_name='Report', header = None, name = ["蔬菜","省","市","批发市场","日期","大宗价","最高价","最低价","交易量","产地"], skiprows = 11,  skipfooter = 3)
    #print(df_temp.head())
    df = df.append(df_temp)
    #print(df.tail())
    i += 1
print(df.tail())

writer = r'E:\peng\2018_01_06.xlsx'
df.to_excel(writer, sheet_name='201801-201806')
print('已导出')
#python E:\peng\test.py'''
