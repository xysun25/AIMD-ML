from ase.io import read, write

atoms = rad('structure.json', format = 'json')
wrte('struc.cif', atoms)
write('struc.vasp', atoms)
