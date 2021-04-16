a = float(input("반지름 입력:"))

circum = 2 * a * 3.14
area = 3.14 * a**2


print("반지름 {}인 원의 면적은 {}, 원의 둘레는 {}".format(a, area, circum))

def circle_area_circum(radius):
    circum = 2 * radius * 3.14
    area = 3.14 * radius**2
    return circum, area

radius = 10
result1, result2 = circle_area_circum(radius)
print("반지름", radius, "인 원의 면적은" , area, "원의 둘레는", circum)