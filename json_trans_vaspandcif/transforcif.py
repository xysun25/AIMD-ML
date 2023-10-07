# from ase.io import read, write

# atoms = read('structure.json', format = 'json')
# write('struc.cif', atoms)
# write('struc.vasp', atoms)

from ase.io import read, write

# 从 Trajectory 文件中读取结构
traj = read('aimd_with_bader.traj', index=':', format='traj')

# # 将每个帧写入单独的 XYZ 文件
# for i, atoms in enumerate(traj):
#     output_file = f'output_{i}.xyz'
#     write(output_file, atoms, format='xyz')

write('out.xyz', traj)
