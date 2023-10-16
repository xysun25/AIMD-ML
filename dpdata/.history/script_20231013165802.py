import dpdata
import numpy as np
import pandas as pd
import matplotlib

outcar_data = dpdata.LabeledSystem("OUTCAR")

# 提取数据
coords = outcar_data["coords"]
forces = outcar_data["forces"]
# temperatures = outcar_data.get_temperatures()
total_energy = outcar_data["energies"]

coords = np.array(coords)
forces = np.array(forces)

dataset = np.hstack([coords,forces])
# dataset_pd = pd.DataFrame('dataset')
# display(dataset_pd)
print(dataset)

# # 
# # with open('dataset.dat','w') as f:
# #     f.write(''.join(dataset_pd.columns))
# # print("coords:")
# # print(coords)

# # print("\nForces:")
# # print(forces)

# # # print("\nTemperatures:")
# # # print(temperatures)

# # print("\nTotal Energy:")
# # print(total_energy)
# array1 = np.array(coords)
# array2 = np.array(forces)

# # # 使用numpy.concatenate函数将它们在第二维度拼接
# # result = np.concatenate((array1, array2), axis=1)
# # result_list = result.tolist()
# # print(result_list)

# # 使用numpy.concatenate函数将它们在第二维度拼接
# result = np.concatenate((array1, array2), axis=1)

# # 将结果写入文件
# output_file = 'output.txt'

# with open(output_file, 'w') as f:
#     for row in result:
#         f.write(' '.join(map(str, row)) + '\n')

# print('Data written to', output_file)



# # # 将原子坐标和原子力写入输出文件
# # with open(output_file, 'w') as f:
# #     f.write(f"Atomic Coordinates:\n")
# #     for i in coords:
# #         f.write(f"{len(i)}\n")
# #         for coord in i:
# #             f.write(f"{coord[0]:.6f} {coord[1]:.6f} {coord[2]:.6f}\n")

# #     f.write(f"\nAtomic Forces:\n")
# #     for f in forces:
# #         f.write(f"{len(f)}\n")
# #         for force in f:
# #             f.write(f"{force[0]:.6f} {force[1]:.6f} {force[2]:.6f}\n")

# # with open(output_filename, 'w') as file:
# #     for angle in angles:
# #         file.write(f'{angle:.2f}\n')