a = 1
b = 2
c = -8

r1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
r2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)

print('해는', r1, '또는', r2)

def root_ex3(a, b, c):
    r3 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
    r4 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)
    return r3, r4

result3, result4 = root_ex3(2, -1, -6)
print('해는', result3, '또는', result4)