import numpy as np

def read_xyz(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_atoms = int(lines[0].strip())
        coords = []
        for i in range(2, num_atoms + 2):
            atom_data = lines[i].strip().split()
            coords.append([float(atom_data[1]), float(atom_data[2]), float(atom_data[3])])
    return np.array(coords)

def calculate_angle(atom1, atom2, atom3):
    vector1 = atom1 - atom2
    vector3 = atom3 - atom2
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector3 = np.linalg.norm(vector3)
    dot_product = np.dot(vector1, vector3)
    angle_radians = np.arccos(dot_product / (norm_vector1 * norm_vector3))
    return np.degrees(angle_radians)


xyz_filename = 'h2o.xyz' 
coordinates = read_xyz(xyz_filename)

# 假设水原子顺序为 O-H-H
# 提取O、H1和H2的坐标
oxygens = coordinates[::3]
hydrogen1 = coordinates[1::3]
hydrogen2 = coordinates[2::3]

# 计算每个水分子的角度
angles = []
for i in range(len(oxygens)):
    angle = calculate_angle(hydrogen1[i], oxygens[i], hydrogen2[i])
    angles.append(angle)

# print("水分子角度分布:")
# print(angles)

output_filename = 'output_angles.txt'  # 输出文件名
with open(output_filename, 'w') as file:
    for angle in angles:
        file.write(f'{angle:.2f}\n')