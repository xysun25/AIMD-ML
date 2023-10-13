import numpy as np

# 读取XYZ文件
def read_xyz(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_atoms = int(lines[0].strip())
        coords = []
        for i in range(2, num_atoms + 2):
            atom_data = lines[i].strip().split()
            coords.append([float(atom_data[1]), float(atom_data[2]), float(atom_data[3])])
    return np.array(coords)

# 计算与 x 轴的夹角
def calculate_angle_with_x_axis(vector):
    unit_x = np.array([1, 0, 0])
    cos_theta = np.dot(vector, unit_x) / (np.linalg.norm(vector) * np.linalg.norm(unit_x))
    angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    return np.degrees(angle_radians)

# 从XYZ文件读取坐标数据
xyz_filename = 'path/to/your/xyz_file.xyz'  # 请替换为你的XYZ文件路径
coordinates = read_xyz(xyz_filename)

# 假设水分子的原子顺序为 O-H-H，可以根据实际情况调整
# 提取氧原子、氢原子1和氢原子2的坐标
oxygens = coordinates[::3]

# 计算每个水分子与 x 轴之间的夹角
angles = []
for i in range(len(oxygens)):
    vector_between_oxygen_and_x_axis = oxygens[i] - np.array([1, 0, 0])
    angle = calculate_angle_with_x_axis(vector_between_oxygen_and_x_axis)
    angles.append(angle)

# 输出角度分布
print("水分子与 x 轴之间的夹角分布:")
print(angles)
