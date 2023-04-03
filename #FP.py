#FP
# menghitung bilangan faktorial menggunakan rekursi
from functools import reduce
def faktorial(n):
    if n == 0:
        return 1
    else:
        return n * faktorial(n-1)

# menghitung jumlah bilangan ganjil dalam sebuah list menggunakan filter dan reduce
bilangan = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bilangan_ganjil = filter(lambda x: x%2 != 0, bilangan)
jumlah_ganjil = reduce(lambda x, y: x+y, bilangan_ganjil)

print(faktorial(5))  # output: 120
print(jumlah_ganjil) # output: 25