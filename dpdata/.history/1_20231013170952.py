import numpy as np

# 创建一个示例的三维数组
three_dim_array = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])

# 获取三维数组的形状
original_shape = three_dim_array.shape

# 计算新的形状，将前两个维度合并为一个，保持第三个维度不变
new_shape = (original_shape[0] * original_shape[1], original_shape[2])

# 使用reshape方法将三维数组变为二维数组
two_dim_array = three_dim_array.reshape(new_shape)

print("原始三维数组:")
print(three_dim_array)
print("\n变为的二维数组:")
print(two_dim_array)
