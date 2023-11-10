import dpdata
import numpy as np

outcar_data = dpdata.LabeledSystem("OUTCAR")

coords = outcar_data["coords"]
forces = outcar_data["forces"
print(coords.shape)
print(forces.shape)
