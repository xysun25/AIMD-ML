import numpy as np
import matplotlib.pyplot as plt

# 读xyz文件
def read_xyz(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_atoms = int(lines[0].strip())
        coords = [
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

# 从xyz文件读取坐标
xyz_filename = 'h2o.xyz'
coordinates = read_xyz(xyz_filename)

# 假设水分子原子顺序为 O-H-H
# 提取O、H1和H2的坐标
oxygens = coordinates[::3]
hydrogen1 = coordinates[1::3]
hydrogen2 = coordinates[2::3]

# 计算每个水分子的平面法向量
normal_vectors = []
for i in range(len(oxygens)):
    normal_vector = calculate_normal_vector(oxygens[i], hydrogen1[i], hydrogen2[i])
    normal_vectors.append(normal_vector)

# 表面z = (1,0,0)
z = np.array([1, 0, 0])

# 计算z与水分子平面法向量间夹角
angles = []
for normal_vector in normal_vectors:
    angle = calculate_angle_between_vectors(z, normal_vector)
    angles.append(angle)

# # 输出夹角分布
# print("表面与水分子平面法向量之间的夹角分布:")
# print(angles)

# 角度分布写入文件
output_filename = 'output_angles.txt' 
with open(output_filename, 'w') as file:
    for angle in angles:
        file.write(f'{angle:.2f}\n')

plt.hist(angles, bins=50, density=True, alpha=0.6, color='b', edgecolor='black')
plt.title('Orientation distribution probability')
plt.xlabel('degree')
plt.ylabel('probability density')
plt.grid(True)
plt.show()
