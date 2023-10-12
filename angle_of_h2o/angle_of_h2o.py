import numpy as np
# 假设你有水分子的坐标，其中 oxygen 是氧原子的坐标
# 这里假设你已经有了水分子的坐标数据
# 例如，oxygen = [x_o, y_o, z_o]

# 计算水分子的取向向量
def calculate_orientation_vector(oxygen):
    # 假设表面在z = 0平面上
    # 计算水分子的氧原子到表面的向量
    surface_normal = np.array([0, 0, 1])  # 假设表面的法向量是z轴方向
    orientation_vector = oxygen - surface_normal
    return orientation_vector

# 使用示例坐标计算取向向量
oxygen = np.array([0.0, 0.0, 1.0])  # 示例水分子的氧原子坐标

orientation_vector = calculate_orientation_vector(oxygen)
print(f"水分子的取向向量: {orientation_vector}")

# 计算取向角度
def calculate_orientation_angle(orientation_vector):
    # 计算取向向量与参考向量之间的夹角，这里参考向量是z轴
    reference_vector = np.array([0, 0, 1])
    cos_angle = np.dot(orientation_vector, reference_vector) / (np.linalg.norm(orientation_vector) * np.linalg.norm(reference_vector))
    angle_in_radians = np.arccos(cos_angle)
    angle_in_degrees = np.degrees(angle_in_radians)
    return angle_in_degrees

orientation_angle = calculate_orientation_angle(orientation_vector)
print(f"水分子的取向角度: {orientation_angle:.2f} 度")
