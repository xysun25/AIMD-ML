import dpdata
import numpy as np
import pandas as pd
import matplotlib

outcar_data = dpdata.LabeledSystem("OUTCAR")

# 提取数据
coords = outcar_data["coords"]

# 获取三维数组的形状
original_shape = coords.shape

# 计算新的形状，将前两个维度合并为一个，保持第三个维度不变
new_shape = (original_shape[0] * original_shape[1], original_shape[2])

# 使用reshape方法将三维数组变为二维数组
two_dim_array = coords.reshape(new_shape)

# 将二维数组写入文件
output_file = 'output.txt'

with open(output_file, 'w') as f:
    for row in two_dim_array:
        f.write(' '.join(map(str, row)) + '\n')

print("新的二维数组已写入文件:", output_file)