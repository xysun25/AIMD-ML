from ase.io import read, write

atoms= read('structure.json', format = 'json')
write('struc.cif', atoms)
write('struc.vasp', atoms)
