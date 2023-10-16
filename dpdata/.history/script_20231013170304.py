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
print(len(coords))
print(len(forces))
