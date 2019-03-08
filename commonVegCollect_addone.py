#只提取价格数据，删除蔬菜名中的空格
import pandas as pd

#打开普通菜汇总表
df = pd.read_excel(r"D:\Data\新发地菜价\新发地普通菜价格汇总.xlsx", sheet_name='普通菜')
print(df.head())

docName = '新发地每日蔬菜价格表-20190308.xls'
doc_address = r'D:\Data\新发地菜价\price_raw'
doc_address += '\\' + docName
print("本次打开的文件名为：", docName)
df_temp = pd.read_excel(
    doc_address,
    sheet_name='Sheet1',
    header=None,
    names=["品种", "最低价（元/斤）", "最高价（元/斤）", "平均价（元/斤）", "上市量（万公斤）", "交易额（万元）"],
    skiprows=3,  #2018.12.22及以前skiprows=2
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

#测试为什么下一段代码无法使用了not supported between instances of 'str' and 'int'
# print(df_temp.head())
# pd.to_numeric(df_temp['最低价（元/斤）'])
# print(df_temp['最低价（元/斤）'].head().dtypes)
# print(df_temp[df_temp['最低价（元/斤）'] > 0])

#删除最低价为0的行
df_temp = df_temp[df_temp['最低价（元/斤）'] > 0]

df = df.append(df_temp)

print(df.tail())
print('还没处理完，别关！！！')
print('还没处理完，别关！！！')
print('还没处理完，别关！！！')
print('还没处理完，别关！！！')
print('--------------------------------------------------------------')

#后缀名为xlsx且写入原文件时时writer必须save和close
writer = pd.ExcelWriter('D:\Data\新发地菜价\新发地普通菜价格汇总.xlsx')
df.to_excel(excel_writer=writer, sheet_name='普通菜', index=False)
writer.save()
writer.close()
print('现在可以关了')
