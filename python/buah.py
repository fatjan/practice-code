keranjang = []

def tambah_buah(fruits):
    for fruit in fruits:
        keranjang.append(fruit)


def tambah_sayur(vegetables):
    for veg in vegetables:
        keranjang.append(veg)

tambah_buah(['apple', 'orange', 'mango'])
tambah_sayur(['cucumber', 'carrot', 'potato'])

print('keranjang', keranjang)
