import time

t_init = time.perf_counter()

key = input("Mulai istigfar, tekan enter untuk melanjutkan. Angka 1 untuk selesai. ")

num = 1

while (not key):
    key = input("Lanjutkan? Press enter for yes ")
    num += 1
    print(num)
    if key:
        break
   

t_final = time.perf_counter()

total_time = t_final - t_init

print("Selesai berdzikir, total istigfar: ", num)
print("Total waktu: %d detik" % total_time)
