import dpdata

outcar_data = dpdata.LabeledSystem("OUTCAR")

output_file = 'data_file.xyz'  # 请替换为你想要保存数据的文件路径
# 提取数据
coords = outcar_data["coords"]
forces = outcar_data["forces"]
# temperatures = outcar_data.get_temperatures()
total_energy = outcar_data["energies"]

outcar_data.to(".xyz",)
# # 输出数据
# print("coords:")
# print(coords)

# print("\nForces:")
# print(forces)

# # print("\nTemperatures:")
# # print(temperatures)

# print("\nTotal Energy:")
# print(total_energy)



# 提取原子坐标和原子力
atomic_coordinates = get_pos(outcar_data)
atomic_forces = get_force(outcar_data)


# 将原子坐标和原子力写入输出文件
with open(output_file, 'w') as f:
    f.write(f"Atomic Coordinates:\n")
    for coords in atomic_coordinates:
        f.write(f"{len(coords)}\n")
        for coord in coords:
            f.write(f"{coord[0]:.6f} {coord[1]:.6f} {coord[2]:.6f}\n")

    f.write(f"\nAtomic Forces:\n")
    for forces in atomic_forces:
        f.write(f"{len(forces)}\n")
        for force in forces:
            f.write(f"{force[0]:.6f} {force[1]:.6f} {force[2]:.6f}\n")
