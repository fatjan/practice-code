input1 = 1
input2 = 10
input3 = 3
x = []
for y in range(input1, input2):
    print(y)
    if y % input3 != 0:
        continue
    print(x)
    x.append(y)

print('\n' + str('-' * 60) + '\n' + 'angka yang bisa dibagi dengan ' + str(input3) + ': \n' + str(x) + '\n')