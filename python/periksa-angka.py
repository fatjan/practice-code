def periksa_angka(daftar, input):
    return input in daftar

daftar = [10, 20, 30, 40, 50]
input = 50

if (periksa_angka(daftar, input)):
    print('ada')
else:
    print(' ga ada ')