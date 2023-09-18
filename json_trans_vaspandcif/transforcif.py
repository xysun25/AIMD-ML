from ase.io import read, write

atoms = read('structure.json', format = 'json')
w rite('struc.cif', atoms)
write('struc.vasp', atoms)
