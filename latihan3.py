print("Hello")
print("Saya sedang belajar Python")

a = 10
b = 3
print("nilai variable a = ", a,b)
print("nilai variable b = ", b)
print("hasil penjumlahan a+b = ", a + b)

a = input("Masukan nilai a : ")
b = input("Masukan nilai b : ")
print("Nilai Variable a = ", a)
print("Nilai Variable b = ", b)


a = int(a)
b = int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))