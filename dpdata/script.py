import dpdata
import numpy as np
d_outcar = dpdata.LabeledSystem("OUTCAR")

atom_names = d_outcar["atom_names"]
coords = d_outcar["coords"]
forces = d_outcar["forces"]

output_file = "vasp_data.txt" 

with open(output_file, "w") as file:
    file.write("原子坐标:\n")
    np.savetxt(file, coords, fmt='%10.6f', delimiter=' ')
    
    file.write("\n力:\n")
    np.savetxt(file, forces, fmt='%10.6f', delimiter=' ')
    
print(f"数据已保存到文件 {output_file}")
