import random

def keluar():
    exit()

def tampilan_awal():
    # pembeli = input('Masukkan nama Anda : ')
    # nama = pembeli.upper()
    print('==========================================')
    print('SELAMAT DATANG',nama,'DI RESTORAN ABCD')
    print('==========================================')
    print('1. MAKAN DISINI?')
    print('2. DIBUNGKUS?')
    print('3. MAKAN DI RUMAH AULIA?')
    print('4. GAJADI KAKK')
    pilih1 = int(input('\nMasukkan pilihan : '))

    if pilih1==1:
        makan_disini()
    elif pilih1==2:
        bungkus()
    elif pilih1==3:
        jenis_menu()
    else:
        keluar()

def makan_disini():
    jumlah_orang= input("untuk berapa orang?")
    no_meja = random.randint(1,20)
    print('Tunggu di meja nomor', no_meja,'\n')
    jenis_menu()

def bungkus():
    print("Anda memilih dibungkus")
    no_antrian = random.randint(1, 30)
    print('No antrian:', no_antrian)
    jenis_menu()

def jenis_menu():
    print('==========')
    print('JENIS MENU')
    print('==========')
    print('1. Makanan')
    print('2. Minuman')
    print('3. kembali')
    pilih2 = int(input('\nMasukkan pilihan : '))
    if pilih2==1:
        jenis_makanan()
    elif pilih2==2:
        jenis_minuman()   
    elif pilih2==3:
        tampilan_awal()

def jenis_makanan():
    print('=====================')
    print('PILIHAN JENIS MAKANAN')
    print('=====================')

    print("1. Indonesian Food")
    print("2. Western Food")
    print("3. Japanese Food")
    print("4. Korean Food")
    print("5. Kembali")
    print("6. Keluar")
    pilih3 = int(input('\nMasukkan pilihan : '))
    
    if pilih3==1:
        indonesia()
    if pilih3==2:
        western()
    if pilih3==3:
        japanese()
    if pilih3==4:
        korean()
    if pilih3==5:
        jenis_makanan()
    if pilih3==6:
        keluar()

def indonesia():
    global pesanan
    global jumlah_pesanan
    global porsi_indo
    global harga
    global total_harga
    global total
    global porsi
    harga = []
    pesanan = []
    total_harga = []
    total = 0
    porsi = []
    stay = True
    while stay:
        print('INDONESIAN FOOD')
        print('===============')
        print('===============')
        print('1. Rendang Padang\t Rp 30000')
        print('2. Nasi Goreng\t\t Rp 15000')
        print('3. Gudeg Yogyakarta\t Rp 25000')
        print('4. Sate Ayam\t\t Rp 35000')
        print('5. kembali')
        print('6. Keluar')
        print('7. pilih minuman')
        #porsi.append(porsi_indo)
        pilih4 = int(input('\nMasukkan pilihan : '))
        if pilih4 == 1:
            porsi_indo = int(input('Jumlah Porsi : '))
            pesanan.append('Rendang Padang')
            porsi.append(porsi_indo)
            total_harga.append(30000*porsi_indo)
            harga.append(30000)
            total = total + (30000*porsi_indo)
        elif pilih4 == 2:
            porsi_indo = int(input('Jumlah Porsi : '))
            porsi.append(porsi_indo)
            harga.append(15000)
            pesanan.append('Nasi Goreng')
            total = total + (15000*porsi_indo)
            total_harga.append(15000*porsi_indo)
        elif pilih4 == 3:
            porsi_indo = int(input('Jumlah Porsi : '))
            pesanan.append('Gudeg Yogyakarta')
            porsi.append(porsi_indo)
            total_harga.append(25000*porsi_indo)
            harga.append(25000)
            total = total + (25000*porsi_indo)
        elif pilih4 == 4:
            porsi_indo = int(input('Jumlah Porsi : '))
            porsi.append(porsi_indo)
            pesanan.append('Sate Ayam')
            harga.append(35000)
            total = total + (35000*porsi_indo)
            total_harga.append(35000*porsi_indo)
        elif pilih4 == 5:
            jenis_makanan()
        elif pilih4 == 6:
            jenis_menu()
        elif pilih4 == 7:
            jenis_minuman()
        else:   
            print("Maaf pilihan yang Anda masukkan tidak ada, silahkan pilih kembali\n")       
            indonesia()

        jumlah_pesanan = len(pesanan)   

        tambah = input('\nApakah ingin menambah pesanan?\n (y/n) : ') 
        if tambah== 'n':
            rinci_bayar()
            stay = False


def western():
    global pesanan
    global jumlah_pesanan
    global porsi_west
    global harga
    global total_harga
    global total
    global porsi
    harga = []
    pesanan = []
    total_harga = []
    total = 0
    porsi = []
    while True:
        print('============')
        print('WESTERN FOOD')
        print('============')
        print('1. PIZZA\t Rp 50000')
        print('2. BURGER\t\t Rp 25000')
        print('3. FRENCH FRIES\t Rp 15000')
        print('4. HOT DOG\t\t Rp20000 ')
        print('5. kembali')
        print('6. Keluar')

        pilih4 = int(input('\nMasukkan pilihan : '))
        if pilih4 == 1:
            porsi_west = int(input('Jumlah Porsi : '))
            porsi.append(porsi_west)
            pesanan.append('PIZZA')
            harga.append(50000)
            total_harga.append(50000*porsi_west)
            total = total + (50000*porsi_west)
        elif pilih4 == 2:
            porsi_west = int(input('Jumlah Porsi : '))
            porsi.append(porsi_west)
            pesanan.append('BURGER')
            harga.append(25000)
            total_harga.append(25000*porsi_west)
            total = total + (25000*porsi_west)
        elif pilih4 == 3:
            porsi_west = int(input('Jumlah Porsi : '))
            porsi.append(porsi_west)
            pesanan.append('FRENCH FRIES')
            total_harga.append(15000*porsi_west)
            harga.append(15000)
            total = total + (15000*porsi_west)
        elif pilih4 == 4:
            porsi_west = int(input('Jumlah Porsi : '))
            porsi.append(porsi_west)
            pesanan.append('HOT DOG')
            harga.append(20000)
            total_harga.append(20000*porsi_west)
            total = total + (20000*porsi_west)
        elif pilih4 == 5:
            jenis_makanan()
        elif pilih4 == 6:
            keluar()
        else:
            print("Maaf pilihan yang Anda masukkan tidak ada, silahkan pilih kembali\n")       
            western()
        
        jumlah_pesanan = len(pesanan)    

        tambah = input('\nApakah ingin menambah pesanan?\n (y/n) : ') 
        if tambah == 'n':
             rinci_bayar()
             break

def japanese():
    global pesanan
    global jumlah_pesanan
    global porsi_japan
    global harga
    global total_harga
    global total
    global porsi
    harga = []
    pesanan = []
    total_harga = []
    total = 0
    porsi = []
    while True:
        print('===============')
        print('JAPANESE FOOD')
        print('===============')
        print('1. SUSHI \t\t Rp 350000')
        print('2. RAMEN\t\t Rp 35000')
        print('3. TAKOYAKI\t\t Rp 15000')
        print('4. CHICKEN KATSU\t Rp25000 ')
        print('5. kembali')
        print('6. Keluar')
    
        pilih4 = int(input('\nMasukkan pilihan : '))
        if pilih4 == 1:
            porsi_japan = int(input('Jumlah Porsi : '))
            porsi.append(porsi_japan)
            pesanan.append('SUSHI')
            harga.append(35000)
            total_harga.append(35000*porsi_japan)
            total = total + (35000*porsi_japan)
        elif pilih4 == 2:
            porsi_japan = int(input('Jumlah Porsi : '))
            porsi.append(porsi_japan)
            pesanan.append('RAMEN')
            harga.append(35000)
            total_harga.append(35000*porsi_japan)
            total = total + (35000*porsi_japan)
        elif pilih4 == 3:
            porsi_japan = int(input('Jumlah Porsi : '))
            porsi.append(porsi_japan)
            pesanan.append('TAKOYAKI')
            harga.append(15000)
            total_harga.append(15000*porsi_japan)
            total = total + (15000*porsi_japan)
        elif pilih4 == 4:
            porsi_japan = int(input('Jumlah Porsi : '))
            porsi.append(porsi_japan)
            pesanan.append('CHICKEN KATSU')
            harga.append(25000)
            total_harga.append(25000*porsi_japan)
            total = total + (25000*porsi_japan)
        elif pilih4 == 5:
            jenis_makanan()
        elif pilih4 == 6:
            keluar()
        else:
            print("Maaf pilihan yang Anda masukkan tidak ada, silahkan pilih kembali\n")       
            japanese()
        jumlah_pesanan = len(pesanan)    

        tambah = input('\nApakah ingin menambah pesanan?\n (y/n) : ') 
        if tambah == 'n':
            rinci_bayar()
            break

def korean():
    global pesanan
    global jumlah_pesanan
    global porsi_korea
    global harga
    global total_harga
    global total
    global porsi
    harga = []
    pesanan = []
    total_harga = []
    total = 0
    porsi = []
    while True:
        print('===============')
        print('KOREAN FOOD')
        print('===============')
        print('1. KIMCHI \t Rp 20000')
        print('2. KIMBAP\t Rp 35000')
        print('3. TTEOKBOKKI \t Rp 20000')
        print('4. DUMPLING\t\t Rp20000 ')
        print('5. kembali')
        print('6. Keluar')
    
        pilih4 = int(input('\nMasukkan pilihan : '))
        if pilih4 == 1:
            porsi_korea = int(input('Jumlah Porsi : '))
            porsi.append(porsi_korea)
            pesanan.append('KIMCHI')
            harga.append(20000)
            total_harga.append(20000*porsi_korea)
            total = total + (20000*porsi_korea)
        elif pilih4 == 2:
            porsi_korea = int(input('Jumlah Porsi : '))
            porsi.append(porsi_korea)
            pesanan.append('KIMBAP')
            harga.append(35000)
            total_harga.append(35000*porsi_korea)
            total = total + (35000*porsi_korea)
        elif pilih4 == 3:
            porsi_korea = int(input('Jumlah Porsi : '))
            porsi.append(porsi_korea)
            pesanan.append('TTEOBOKKI')
            harga.append(15000)
            total_harga.append(15000*porsi_korea)
            total = total + (15000*porsi_korea)
        elif pilih4 == 4:
            porsi_korea = int(input('Jumlah Porsi : '))
            porsi.append(porsi_korea)
            pesanan.append('DUMPLING')
            harga.append(20000)
            total_harga.append(20000*porsi_korea)
            total = total + (20000*porsi_korea)
        elif pilih4 == 5:
            jenis_makanan()
        elif pilih4 == 6:
            keluar()
        else:
    
            print("Maaf pilihan yang Anda masukkan tidak ada, silahkan pilih kembali\n")       
            korean()
        jumlah_pesanan = len(pesanan)    

        tambah = input('\nApakah ingin menambah pesanan?\n (y/n) : ') 
        if tambah == 'n':
            rinci_bayar()
            break

def jenis_minuman():
    print('=====================')
    print('PILIHAN JENIS MINUMAN')
    print('=====================')

    print("1. COLD DRINK")
    print("2. HOT DRINK")
    print("Kembali")
    print("Keluar")
    pilih8 = int(input('\nMasukkan pilihan : '))

    if pilih8==1:
        cold()
    if pilih8==2:
        hot()

def cold():
    global pesanan
    global jumlah_pesanan
    global porsi_cold
    global harga
    global total_harga
    global total
    global porsi
    harga = []
    pesanan = []
    total_harga = []
    total = 0
    porsi = []
    while True:
        print('===============')
        print('COLD DRINK')
        print('===============')
        print('1. ORANGE JUICE\t Rp 15000')
        print('2. SOFT DRINK\t\t Rp 15000')
        print('3. ICE TEA\t Rp 15000')
        print('4. ICE OCHA TEA\t\t Rp 15000')
        print('5. SOJUU\t Rp 60000')
        print('6. ICE COFFE LATTE\t Rp 25000')
        print('7. COLD WATER\t Rp 10000')
        print('8. Keluar')
    
        pilih9 = int(input('\nMasukkan pilihan : '))
        if pilih9 == 1:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('ORANGE JUICE')
            harga.append(15000)
            total_harga.append(15000*porsi_cold)
            total = total + (15000*porsi_cold)
        elif pilih9 == 2:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('SOFT DRINK')
            harga.append(15000)
            total_harga.append(15000*porsi_cold)
            total = total + (15000*porsi_cold)
        elif pilih9 == 3:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('ICE TEA')
            harga.append(15000)
            total_harga.append(15000*porsi_cold)
            total = total + (15000*porsi_cold)
        elif pilih9 == 4:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('ICE OCHA TEA')
            harga.append(15000)
            total_harga.append(15000*porsi_cold)
            total = total + (15000*porsi_cold)
        elif pilih9 == 5:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('SOJU')
            harga.append(60000)
            total_harga.append(60000*porsi_cold)
            total = total + (60000*porsi_cold)
        elif pilih9 == 6:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('ICE COFFE LATTE')
            harga.append(60000)
            total_harga.append(60000*porsi_cold)
            total = total + (60000*porsi_cold)
        elif pilih9 == 7:
            porsi_cold = int(input('Jumlah Porsi : '))
            porsi.append(porsi_cold)
            pesanan.append('COLD WATER')
            harga.append(10000)
            total_harga.append(10000*porsi_cold)
            total = total + (10000*porsi_cold)
        else:
            print("Maaf pilihan yang Anda masukkan tidak ada, silahkan pilih kembali\n")       
            cold()
        jumlah_pesanan = len(pesanan)    

        tambah = input('\nApakah ingin menambah pesanan?\n (y/n) : ') 
        if tambah == 'n':
            rinci_bayar()
            break

def hot():
    global pesanan
    global jumlah_pesanan
    global porsi_hot
    global harga
    global total_harga
    global total
    global porsi
    harga = []
    pesanan = []
    total_harga = []
    total = 0
    porsi = []
    while True:
        print('===============')
        print('HOT DRINK')
        print('===============')
        print('1. HOT TEA\t Rp 15000')
        print('2. HOT MATCHA LATTE\t\t Rp 20000')
        print('3. HOT COFFEE LATTE\t Rp 20000')
        print('4. HOT OCHA TEA\t\t Rp 15000')
        print('5. HOT CHOCOLATE\t Rp 20000')
        print('6. HOT WATER\t Rp 10000')
        print('7. Keluar')
    
        pilih10 = int(input('\nMasukkan pilihan : '))
        porsi_hot = int(input('Jumlah Porsi : '))
        if pilih10 == 1:
            porsi.append(porsi_hot)
            pesanan.append('HOT TEA')
            harga.append(15000)
            total_harga.append(15000*porsi_hot)
            total = total + (15000*porsi_hot)
        elif pilih10 == 2:
            porsi_hot = int(input('Jumlah Porsi : '))
            porsi.append(porsi_hot)
            pesanan.append('HOT MATCHA LATTE')
            harga.append(20000)
            total_harga.append(20000*porsi_hot)
            total = total + (20000*porsi_hot)
        elif pilih10 == 3:
            porsi_hot = int(input('Jumlah Porsi : '))
            porsi.append(porsi_hot)
            pesanan.append('HOT COFFE LATTE')
            harga.append(20000)
            total_harga.append(20000*porsi_hot)
            total = total + (20000*porsi_hot)
        elif pilih10 == 4:
            porsi_hot = int(input('Jumlah Porsi : '))
            porsi.append(porsi_hot)
            pesanan.append('HOT OCHA TEA')
            harga.append(15000)
            total_harga.append(15000*porsi_hot)
            total = total + (15000*porsi_hot)
        elif pilih10 == 5:
            porsi_hot = int(input('Jumlah Porsi : '))
            porsi.append(porsi_hot)
            pesanan.append('HOT CHOCOLATE')
            harga.append(20000)
            total_harga.append(20000*porsi_hot)
            total = total + (20000*porsi_hot)
        elif pilih10 == 6:
            porsi_hot = int(input('Jumlah Porsi : '))
            porsi.append(porsi_hot)
            pesanan.append('HOT WATER')
            harga.append(10000)
            total_harga.append(10000*porsi_hot)
            total = total + (10000*porsi_hot)
        else:
            print("Maaf pilihan yang Anda masukkan tidak ada, silahkan pilih kembali\n")       
            hot()
        jumlah_pesanan = len(pesanan)    

        tambah = input('\nApakah ingin menambah pesanan?\n (y/n) : ') 
        if tambah == 'n':
            rinci_bayar()
            break

        

        

def rinci_bayar():
    print ('1. Rincian Pemesanan')
    print ('2. Menu Pembayaran')
    print ('3. Menu Utama')
    print('4. pilih minum')
    print('5. cetak struk')

    pilih5 = int(input('\nMasukkan Pilihan : '))
    print()
    if pilih5==1:
        rincian_pemesanan()
    # elif pilih5==2:
    #     menu_pembayaran()
    elif pilih5==3:
        tampilan_awal()
    elif pilih5== 4:
        jenis_minuman()


def rincian_pemesanan():
    print('No.\t pesanan makan\t\tJumlah Porsi\t Harga \t Total Harga')
    for i in range (0, jumlah_pesanan):
       print (i+1,'\t',pesanan[i], '\t  ',porsi[i],'\t\t', harga[i],'\t    ',total_harga[i])
     
    print('==========================================================================')
    print('Total \t\t\t\t\t\t\t   ', total )
    
#agar semua tercetak di rincian pemesanan?
    
pembeli = input('Masukkan Nama Anda : ')
nama = pembeli.upper()
tampilan_awal()


# import datetime  
# dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
    # datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
    # datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
# invoice = str(dt)  # unique invoice
# t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
    # datetime.datetime.now().day)  # date
# d = str(t)  # date
# u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
    # datetime.datetime.now().second)  # time
# e = str(u)  # t
#d = date and e = t
#invoice
# print(invoice +  (" + nama + "),nama)  
# print("=============================================================")
# print("\nCASTLE BLACK CAFE\t\t\t\tINVOICE")
# print("\n\nInvoice: " + invoice + "\t\tDate: " + d + "\n\t\t\t\t\tTime: " + e + "")
# print("\nName of Customer: " + str(nama) + "")
# print("\n=============================================================")
# print("\nFood Name\t\tQUANTITY\t\tFood PRICE\t\t\tTOTAL")
# print("\n-------------------------------------------------------------\n")
# for i in range(len(jumlah_pesanan)):
    # Total = harga[i]*porsi[i]
    # total_harga.append(total)
    # food_names =pesanan[i]
    # qunatitys = porsi[i]
    # prize = total_harga[i]
    # Totals = total
    # s = "{:^12}{:^12}{:^12}{:^12}".format(food_names,qunatitys,prize,Totals)
    # print(
    # str("\n" + str(food_name[Tlist[i]]) + "\t\t\t" + str(qun[i]) + "\t\t\t\t " + str(food[Tlist[i]]) + "\t\t\t\t " + str(Total)))
    # print(str("\n{:^12}\t{:^12}\t{:^12}\t{:^12}".format(food_names,qunatitys,prize,Totals)))








        



