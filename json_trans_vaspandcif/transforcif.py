from ase.io import read, write

atoms = rad('structure.json', format = 'json')
write('struc.cif', atoms)
write('struc.vasp', atoms)
