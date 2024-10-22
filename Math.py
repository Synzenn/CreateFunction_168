import math #library untuk operasi mtk

#Rumus dari luas lingkaran
luas_lingkaran = lambda r: math.pi * r*r
#mendefinisikan fungsi yang oendek tanpa harys menggunakan akta kunci def seperti pada fungsi biasa

#contoh penggunaan dari rumus diatas
jari_jari = 7
area = luas_lingkaran(jari_jari)
#area = luas lingkaran

print(f"luas lingkaran dengan jari_jari {jari_jari} adalah {area:.2f}")