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

# 计算平面的法向量
def calculate_normal_vector(atom1, atom2, atom3):
    vector1 = atom1 - atom2
    vector2 = atom2 - atom3
    normal_vector = np.cross(vector1, vector2)
    return normal_vector

# 计算两个向量之间的夹角
def calculate_angle_between_vectors(vector1, vector2):
    cos_theta = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    angle_radians = np.arccos(np.clip(cos_theta, -1.0, 1.0))
    return np.degrees(angle_radians)

# 从XYZ文件读取坐标数据
xyz_filename = 'h2o.xyz'  # 请替换为你的XYZ文件路径
coordinates = read_xyz(xyz_filename)

# 假设水分子的原子顺序为 O-H-H，可以根据实际情况调整
# 提取氧原子、氢原子1和氢原子2的坐标
oxygens = coordinates[::3]
hydrogen1 = coordinates[1::3]
hydrogen2 = coordinates[2::3]

# 计算每个水分子的平面法向量
normal_vectors = []
for i in range(len(oxygens)):
    normal_vector = calculate_normal_vector(oxygens[i], hydrogen1[i], hydrogen2[i])
    normal_vectors.append(normal_vector)

# 定义目标向量 (1, 0, 0)
target_vector = np.array([1, 0, 0])

# 计算向量 (1, 0, 0) 与水分子平面法向量之间的夹角
angles = []
for normal_vector in normal_vectors:
    angle = calculate_angle_between_vectors(target_vector, normal_vector)
    angles.append(angle)

# 输出夹角分布
print("向量 (1, 0, 0) 与水分子平面法向量之间的夹角分布:")
print(angles)