for i in range(1, 11):
    if (i %2 == 0) :
        continue

print(i)
i += 1

even_list = []
for i in range(1, 11):
    # print(i)

    if (i % 2 == 0):
         even_list.append(i)
print(even_list)