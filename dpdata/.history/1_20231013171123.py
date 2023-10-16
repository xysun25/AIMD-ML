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
two_dim_array = three_dim_array.reshape(new_shape)

print("原始三维数组:")
print(coords)
print("\n变为的二维数组:")
print(two_dim_array)
