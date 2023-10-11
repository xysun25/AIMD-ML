import numpy as np
import matplotlib.pyplot as plt
from ase.io import read
from ase.geometry.analysis import Analysis
from ase.geometry import cell_to_cellpar

# 1. 读取XYZ轨迹文件
traj = read('h2o.xyz', format='xyz', index=slice(None))

# 2. 定义表面水分子
# 假设表面水分子在z坐标小于一定值时认为是表面分子
surface_height_threshold = 10.0  # 调整阈值以匹配你的系统
surface_molecules = [i for i, atoms in enumerate(traj) if np.max(atoms.positions[:, 2]) < surface_height_threshold]

# 3. 计算水分子之间的角度
angles = []

for i in surface_molecules:
    atoms = traj[i]
    analysis = Analysis(atoms)
    for a in range(len(atoms)):
        neighbors = analysis.get_neighbors(a)
        for j in range(len(neighbors) - 1):
            for k in range(j + 1, len(neighbors)):
                angle = analysis.get_angle(a, neighbors[j], neighbors[k])
                angles.append(angle)

# 4. 绘制角度分布直方图
plt.hist(angles, bins=50, range=(0, 180))
plt.xlabel('角度 (度)')
plt.ylabel('频率')
plt.title('表面水分子角度分布')
plt.show()
