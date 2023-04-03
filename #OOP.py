#OOP
# membuat kelas PersegiPanjang
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

# membuat objek persegi panjang
pp = PersegiPanjang(5, 3)

# mengakses method pada objek persegi panjang
print(pp.hitung_luas())      # output: 15
print(pp.hitung_keliling())  # output: 16
