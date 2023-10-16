import dpdata

outcar_data = dpdata.LabeledSystem("OUTCAR")

# 提取数据
coords = outcar_data["coords"]
forces = outcar_data["forces"]
# temperatures = outcar_data.get_temperatures()
total_energy = outcar_data["energies"]

# 输出数据
print("coords:")
print(coords)

print("\nForces:")
print(forces)

# print("\nTemperatures:")
# print(temperatures)

print("\nTotal Energy:")
print(total_energy)
