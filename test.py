import pandas as pd
#"D:\Data\新发地菜价\新发地每日蔬菜价格表-20160803.xls"
#"D:\Github\xfd_vegetable_price\test.py"
#python D:\Github\xfd_vegetable_price\test.py
specialVegList = ['新发地特菜价格表-20160811.xls',
'新发地特菜价格表-20160831.xls',
'新发地特菜价格表-20160913.xls',
'新发地特菜价格表-20160921.xls',
'新发地特菜价格表-20160930.xls',
'新发地特菜价格表-20161010.xls',
'新发地特菜价格表-20161030.xls',
'新发地特菜价格表-20161112.xls',
'新发地特菜价格表-20161121.xls',
'新发地特菜价格表-20161201.xls',
'新发地特菜价格表-20170110.xls',
'新发地特菜价格表-20170301.xls',
'新发地特菜价格表-20170411.xls',
'新发地特菜价格表-20170429.xls',
'新发地特菜价格表-20170511.xls',
'新发地特菜价格表-20170630.xls',
'新发地特菜价格表-20170712.xls',
'新发地特菜价格表-20170801.xls',
'新发地特菜价格表-20170821.xls',
'新发地特菜价格表-20170825.xls',
'新发地特菜价格表-20170831.xls',
'新发地特菜价格表-20170905.xls',
'新发地特菜价格表-20170912.xls',
'新发地特菜价格表-20170921.xls',
'新发地特菜价格表-20170930.xls',
'新发地特菜价格表-20171005.xls',
'新发地特菜价格表-20171011.xls',
'新发地特菜价格表-20171016.xls',
'新发地特菜价格表-20171021.xls',
'新发地特菜价格表-20171031.xls',
'新发地特菜价格表-20171106.xls',
'新发地特菜价格表-20171122.xls',
'新发地特菜价格表-20171127.xls',
'新发地特菜价格表-20171201.xls',
'新发地特菜价格表-20171205.xls',
'新发地特菜价格表-20171211.xls',
'新发地特菜价格表-20171216.xls',
'新发地特菜价格表-20171220.xls',
'新发地特菜价格表-20171227.xls',
'新发地特菜价格表-20180106.xls',
'新发地特菜价格表-20180110.xls',
'新发地特菜价格表-20180116.xls',
'新发地特菜价格表-20180120.xls',
'新发地特菜价格表-20180126.xls',
'新发地特菜价格表-20180201.xls',
'新发地特菜价格表-20180210.xls',
'新发地特菜价格表-20180211.xls',
'新发地特菜价格表-20180228.xls',
'新发地特菜价格表-20180310.xls',
'新发地特菜价格表-20180316.xls',
'新发地特菜价格表-20180321.xls',
'新发地特菜价格表-20180325.xls',
'新发地特菜价格表-20180331.xls',
'新发地特菜价格表-20180401.xls',
'新发地特菜价格表-20180406.xls',
'新发地特菜价格表-20180410.xls',
'新发地特菜价格表-20180416.xls',
'新发地特菜价格表-20180421.xls',
'新发地特菜价格表-20180426.xls',
'新发地特菜价格表-20180501.xls',
'新发地特菜价格表-20180507.xls',
'新发地特菜价格表-20180511.xls',
'新发地特菜价格表-20180516.xls',
'新发地特菜价格表-20180521.xls',
'新发地特菜价格表-20180526.xls',
'新发地特菜价格表-20180531.xls',
'新发地特菜价格表-20180607.xls',
'新发地特菜价格表-20180612.xls',
'新发地特菜价格表-20180616.xls',
'新发地特菜价格表-20180622.xls',
'新发地特菜价格表-20180626.xls',
'新发地特菜价格表-20180706.xls',
'新发地特菜价格表-20180716.xls',
'新发地特菜价格表-20180720.xls'
]
df = pd.read_excel('D:\Data\新发地菜价\特菜\新发地特菜价格表-20160811.xls', sheet_name='Sheet1', header = 2, skipfooter=3)
#print(df.describe())
df['日期'] = '2016-08-11'
#print(df.head())
#print(df)
#print(df.describe())
print(df.head())

for i in range(1, len(specialVegList)):
    docName = specialVegList[i]
    doc_address = r'D:\Data\新发地菜价\特菜'
    doc_address += '\\' + docName
    print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(doc_address, sheet_name='Sheet1', header = 2, skipfooter=3)
    #print(df_temp.head())
    colDate = str(docName[9:13]) + '-' + str(docName[13:15]) + '-' + str(docName[15:17])
    print('本次添加的colDate为：', colDate)
    #print(str(specialVegList[9:13]) + '-' + str(specialVegList[13:14] + '-' + str(specialVegList[15:16])
    #print(type(colDate))
    df_temp['日期'] = colDate

    df = df.append(df_temp)
    i += 1

print(df.tail())
#writer = pd.ExcelWriter('D:\Data\新发地菜价\特菜\特菜价格汇总.xls')
writer = r'D:\Data\新发地菜价\特菜\特菜价格汇总.xls'
print(type(writer))
pd.DataFrame.to_excel(writer,sheet_name='特菜价格汇总')
