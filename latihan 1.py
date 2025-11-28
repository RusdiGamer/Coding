# Latihan menghitung luas dan keliling
# Persegi

print("Menghitung luas dan keliling persegi\n")
p = int(input("Masukan diameter persegi :"))
print("\nDiameter persegi:", p, "cm")

#rumus
luas = p * p
keliling = 4 * p

print("Luas Persegi", luas, "cm")
print("Keliling Persegi", keliling, "cm")

#Persegi Panjang

print("\nMenghitung luas dan keliling persegi panjang\n")
p = int(input("Masukan panjang persegi:"))
l = int(input("Masukan lebar persegi:"))
print("\nPanjang persegi:", p, "cm")
print("Lebar persegi", l, "cm")

#rumus
luas = p * l
keliling = 2 *( p + l )

print("Luas Persegi", luas, "cm")
print("Keliling Persegi", keliling, "cm")

# Segitiga

print("\nMenghitung luas dan keliling segitiga\n")
a = int(input("Masukan  alas/ sisi A:"))
t = int(input("Masukan tinggi/ sisi B:"))
c = int(input("Masukan sisi C:"))
print("\nAlas segitiga/ sisi A:", a, "cm")
print("Tinggi segitiga/ sisi B:", t, "cm")
print("Sisi C:", c, "cm")

#rumus
luas = a * t / 2
keliling = a + t + c

print("Luas Segitiga", luas, "cm")
print("Keliling Segitiga", keliling, "cm")

#Lingkaran

print("\nMenghitung luas dan keliling Lingkaran\n")
r = int(input("Masukan jari-jari lingkaran :"))
print("\nJari-jari lingkaran:", r, "cm")

from decimal import Decimal #desimal

#rumus
d = 2 * r #diameter
pĥi = 3.14 # 22/7 kurang akurat karena bakal diubah ke desimal
l = pĥi * (r ** 2) #luas
k = 2 * (pĥi * r) #keliling

#menjadikanya desimal
dl = Decimal(l)
dk = Decimal(k)

#membuat hanya 2 digit setelah 0 yang akan ditulis
il = dl.quantize(Decimal("0.00"))
ik = dk.quantize(Decimal("0.00"))

print("Diameter Lingkaran", d, "cm")
print("Luas Lingkaran", il, "cm")
print("Keliling Lingkaran", ik, "cm")