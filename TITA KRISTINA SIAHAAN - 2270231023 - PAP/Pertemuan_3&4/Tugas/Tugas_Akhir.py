#Tugas Akhir Laporan Praktikum Aplikasi Kasir

print("-------------------- Cafe Tita Kristina --------------------")
print("-- Jl. Unkris, Jaticempaka, Pondok Gede, Jawa Barat 13620 --")
print("---------------------- 0878 5556 3897 ----------------------")

nama = input("Selamat datang! Mohon memberikan nama anda!: ")

def fungsimakanan():
   global totalmkn
   global Banyak
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Roti - Rp 5000")
   print("2. Donat - Rp 6000")
   print("3. Kue - Rp 10000")
   nomor=int(input("Masukan Pilihan: "))
   Banyak= int(input("Berapa Banyak: "))
   
   if nomor==1:
       totalmkn=Banyak*5000
       print (Banyak,"buah Roti = Rp", totalmkn)
       mkn=("Roti")
   elif nomor==2:
       totalmkn=Banyak*6000
       print (Banyak,"buah Donat = Rp", totalmkn)
       mkn=("Donat")
   elif nomor==3:
       totalmkn=Banyak*10000
       print (Banyak, "buah Kue = Rp", totalmkn)
       mkn=("Kue")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Kopi - Rp 2000")
   print("2. Susu - Rp 3500")
   print("3. Matcha - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*2000
       print (gelas,"gelas Kopi = Rp", totalmnm)
       mnm=(" Gelas Kopi")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, "gelas Susu = Rp", totalmnm)
       mnm=("Susu")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, "gelas Matcha = Rp", totalmnm)
       mnm=("Matcha")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n===================== Struk Pembelian ======================")
print("============================================================")
print("==================== Cafe Tita Kristina ====================")
print("== Jl. Unkris, Jaticempaka, Pondok Gede, Jawa Barat 13620 ==")
print("====================== 0878 5556 3897 ======================")
print("Nama\t\t:",nama)
print("Tanggal\t\t: 18 November 2022")
print("Beli\t\t:",Banyak,mkn,"( Rp", totalmkn,")")
print("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print("Tagihan\t\t: Rp",totalsemua)
print("Dibayar\t\t: Rp",uang)
print("Kembalian\t: Rp",kembalian)
print("============================================================")
print("============================================================")