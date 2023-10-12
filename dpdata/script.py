import dpdata

d_outcar = dpdata.LabeledSystem("OUTCAR")
coords = d_outcar["coords"]

d_outcar.to("lammps/lmp", "conf.lmp", frame_idx=0)