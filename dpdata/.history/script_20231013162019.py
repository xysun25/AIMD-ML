import dpdata

outcar_data = dpdata.LabeledSystem("OUTCAR")

# 提取数据
coords = outcar_data["coords"]
forces = outcar_data["forces"]
# temperatures = outcar_data.get_temperatures()
total_energy = outcar_data["energies"]

# # 输出数据
# print("coords:")
# print(coords)

# print("\nForces:")
# print(forces)

# # print("\nTemperatures:")
# # print(temperatures)

# print("\nTotal Energy:")
# print(total_energy)

# 创建一个dpdata.Dataset对象以存储数据
dataset = dpdata.Dataset()

# 将数据添加到Dataset中
dataset.atoms.append(atomic_coordinates)
dataset.forces.append(atomic_forces)
dataset.properties['energy'] = total_energy

# 指定输出文件路径
output_file = 'dataset.xyz'  # 请替换为你想要保存数据的文件路径

# 将数据写入输出文件
dataset.to_deepmd_npy(output_file)

# 可选：将数据以XYZ格式写入文件
dataset.to_deepmd_xyz('dataset.xyz')