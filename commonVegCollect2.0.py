#只提取价格数据，删除蔬菜名中的空格
import pandas as pd
commonVegList = [
    '新发地每日蔬菜价格表-20190216.xls', '新发地每日蔬菜价格表-20190217.xls',
    '新发地每日蔬菜价格表-20190218.xls', '新发地每日蔬菜价格表-20190219.xls',
    '新发地每日蔬菜价格表-20190220.xls', '新发地每日蔬菜价格表-20190221.xls',
    '新发地每日蔬菜价格表-20190222.xls', '新发地每日蔬菜价格表-20190223.xls',
    '新发地每日蔬菜价格表-20190224.xls', '新发地每日蔬菜价格表-20190225.xls',
    '新发地每日蔬菜价格表-20190226.xls', '新发地每日蔬菜价格表-20190227.xls',
    '新发地每日蔬菜价格表-20190228.xls', '新发地每日蔬菜价格表-20190301.xls',
    '新发地每日蔬菜价格表-20190302.xls', '新发地每日蔬菜价格表-20190303.xls',
    '新发地每日蔬菜价格表-20190304.xls', '新发地每日蔬菜价格表-20190305.xls'
]

#提取第一个文件
df = pd.read_excel(
    r'D:\Data\新发地菜价\price_raw\新发地每日蔬菜价格表-20190215.xls',
    sheet_name='Sheet1',
    header=None,
    names=["品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万公斤）", "交易额（万元）"],
    skiprows=2,
    skipfooter=3,
    usecols='A:F')
#添加日期列
df['日期'] = '2019-02-15'
#删除蔬菜名称中的空格
df['品种'] = df['品种'].str.replace(' ', '')
#删除最低价为0和空格的行
df = df[df['最低价（元/斤）'] > 0]
# print(df.head())
# print(df.tail())

#提取其他文件
for i in range(1, len(commonVegList)):
    print('i=', i)
    docName = commonVegList[i]
    doc_address = r'D:\Data\新发地菜价\price_raw'
    doc_address += '\\' + docName
    print("本次打开的文件名为：", docName)
    df_temp = pd.read_excel(
        doc_address,
        sheet_name='Sheet1',
        header=None,
        names=[
            "品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万公斤）", "交易额（万元）"
        ],
        skiprows=2,
        skipfooter=3,
        usecols='A:F')
    #print(df_temp.head())
    colDate = str(docName[11:15]) + '-' + str(docName[15:17]) + '-' + str(
        docName[17:19])
    print('本次添加的colDate为：', colDate)
    #print(type(colDate))
    df_temp['日期'] = colDate
    #删除蔬菜名中的空格
    df_temp['品种'] = df_temp['品种'].str.replace(' ', '')
    #删除最低价为0的行
    df_temp = df_temp[df_temp['最低价（元/斤）'] > 0]
    df = df.append(df_temp)
    #print(df.tail())
    i += 1

print(df.tail())

#后缀名可为xlsx
writer = r'D:\Data\新发地菜价\普通菜价格汇总20190215-0305.xls'
df.to_excel(writer, sheet_name='普通菜价格汇总', index=False)
