import dpdata

outcar_data = dpdata.LabeledSystem("OUTCAR")

output_file = 'data_file.xyz' 
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

# 将原子坐标和原子力写入输出文件
with open(output_file, 'w') as f:
    f.write(f"Atomic Coordinates:\n")
    for i in coords:
        f.write(f"{len(i)}\n")
        for coord in i:
            f.write(f"{coord[0]:.6f} {coord[1]:.6f} {coord[2]:.6f}\n")

    f.write(f"\nAtomic Forces:\n")
    for f in forces:
        f.write(f"{len(f)}\n")
        for force in f:
            f.write(f"{force[0]:.6f} {force[1]:.6f} {force[2]:.6f}\n")
