# -*- coding: utf-8 -*-
import os
import pandas as pd

# 指定要合并的文件夹路径
folder_path = './'

# 指定要合并的文件扩展名
file_extension = '.xls'

# 获取文件夹中所有指定扩展名的文件
all_files = [f for f in os.listdir(folder_path) if f.endswith(file_extension)]

# 将所有文件读入一个 DataFrame 中
# 出现编码错误时检查是否是使用pd.read_csv了 
df = pd.concat([pd.read_excel(os.path.join(folder_path, f)) for f in all_files], ignore_index=True)

# # 数据清洗，删除不需要的行
# condition = input("请输入需要清洗的条件：")
# df = df[df['列名'].str.contains(condition)]

# 删除空白行
df = df.dropna(how='all')

# 将合并后的 DataFrame 写入新文件中
output_file = './merged_data.csv'
df.to_csv(output_file, index=False)
