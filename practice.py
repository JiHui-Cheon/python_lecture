def print_root_ex(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return(r1, r2)

a = 2
b = -1
c = -6

x_1, x_2 = print_root_ex(a,b,c)

print('해는 {} 또는 {}'.format(x_1,x_2))

