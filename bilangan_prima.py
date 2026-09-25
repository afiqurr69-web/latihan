batas_bawah = int(input("Masukkan batas bawah: "))
batas_atas = int(input("Masukkan batas atas: "))

daftar_prima = [] 
total_prima = 0    

# 2. Perulangan dari batas_bawah sampai batas_atas
for angka in range(batas_bawah, batas_atas + 1):
    if angka > 1:
        is_prima = True
        
        for i in range(2, angka):
            if angka % i == 0: 
                is_prima = False
                break
        
    
        if is_prima:
            daftar_prima.append(angka)
            total_prima += 1

print("Bilangan prima yang ditemukan:", daftar_prima)
print("Jumlah total bilangan prima:", total_prima)