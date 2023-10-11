import numpy as np
from ase.io import read
from ase.geometry import cell_to_cellpar
from ase.neighborlist import NeighborList

# 1. 读取XYZ轨迹文件
traj = read('your_xyz_trajectory.xyz', format='xyz', index=slice(None))

# 2. 定义表面水分子
# 假设表面水分子在z坐标小于一定值时认为是表面分子
surface_height_threshold = 10.0  # 调整阈值以匹配你的系统
surface_molecules = [i for i, atoms in enumerate(traj) if np.max(atoms.positions[:, 2]) < surface_height_threshold]

# 3. 计算水分子之间的角度
angles = []

for i in surface_molecules:
    atoms = traj[i]
    nl = NeighborList([2.0] * len(atoms), self_interaction=False, bothways=True)
    nl.update(atoms)

    for a in range(len(atoms)):
        indices, offsets = nl.get_neighbors(a)
        for j in range(len(indices) - 1):
            for k in range(j + 1, len(indices)):
                angle = atoms.get_angle(indices[j], a, indices[k])
                angles.append(np.degrees(angle))

# 4. 输出角度信息
for angle in angles:
    print(f"角度: {angle:.2f} 度")

# 5. 可选：统计和可视化角度信息
angle_array = np.array(angles)
mean_angle = np.mean(angle_array)
std_dev = np.std(angle_array)

print(f"平均角度: {mean_angle:.2f} 度")
print(f"标准差: {std_dev:.2f}")

# 6. 绘制角度分布直方图
import matplotlib.pyplot as plt

plt.hist(angles, bins=50, range=(0, 180))
plt.xlabel('角度 (度)')
plt.ylabel('频率')
plt.title('表面水分子角度分布')
plt.show()
