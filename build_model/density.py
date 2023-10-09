# A = 0.1 nm = 10-8 cm
a = 10.41
b = 9.07
c = 15.0

# g/mol
f1_m = 127
f2_m = 280

# g/cm3
density = 1.4

box_ol = a * b * c / 10**24  # cm3
avo_con = 6.02214076 * 10**23  # Avogadro constant

n = density * box_vol * avo_con / (f1_m + f2_m)
print(n)
