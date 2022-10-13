def welcome():
    print(' ')
    print('===================================')
    print('== Toko Buku Gramedia Al-Hidayah ==')
    print('===================================')
    menu()

def menu():
    print('\n============================================================')
    print('[1]Pilih 1 untuk melihat daftar menu buku yang sedang diskon')
    print('[2]Pilih 2 untuk membeli buku')
    print('[3]Pilih 3 untuk melihat ketentuan diskon buku')
    print('[0]Pilih 0 untuk keluar dari aplikasi')
    print('============================================================')

    pilih  = input('Masukkan Nomor Pilihan Anda : ')

    if pilih == '1':
       daftar_buku()
    elif pilih == '2':
       beli_buku()
    elif pilih == '3':
       ketentuan_diskon()
    elif pilih == '0':
       keluar()
    else:
       print('\nAngka yang Anda masukan tidak dikenal\nAnda kami kembalikan ke menu utama\n')     
       menu()

def daftar_buku():
    print('\n============================================================')
    print('!! Daftar Buku Yang Sedang Diskon !!')
    print('1. The Wish of Dragon\t[Harga Normal: Rp50000]')
    print('2. Emperor Domination\t[Harga Normal: Rp100000]')
    print('3. Legend of Fution\t[Harga Normal: Rp150000]')
    print('4. Love Letter\t[Harga Normal: Rp120000]')
    print('5. Miracle in Cell No 7\t[Harga Normal: Rp500000]')
    print('===========================================================')
    back_to_menu()

def ketentuan_diskon():
    print('\n===================================================================================')
    print('!! Ketentuan Diskon Toko Buku Gramedia Al-Hidayah !!')
    print('1. Diskon buku akan berlaku sebanyak 15% jika membeli lebih dari atau sama dengan 1')
    print('2. Diskon buku akan berlaku sebanyak 25% jika membeli lebih dari 5 hingga maksimal 10')
    print('3. Diskon buku akan berlaku sebanyak 50% jika membeli lebih dari 10')
    print('====================================================================================')
    back_to_menu()

def beli_buku():
    print('\nDaftar Buku Yang Sedang Diskon')
    print('1. The Wish of Dragon\t[Kode: twd]')
    print('2. Emperor Domination\t[Kode: edn]')
    print('3. Legend of Fution\t[Kode: lof]')
    print('4. Love Letter\t[Kode: lot]')
    print('5. Miracle in Cell No 7\t[Kode: mc7]\n')

    print('[1] Pilih No 1 Jika ingin melanjutkan')
    print('[0] Pilih No 0 Jika ingin kembali ke menu utama')

    pilih = input('Pilih salah satu angka jika Anda ingin melanjutkan? : ')
    if pilih == '1':
       hitung_harga()
    elif pilih == '0':
       menu()

def hitung_harga():
    nama = input('\nMasukkan Nama Pembeli\t : ')
    kode = input('Masukkan Kode Buku\t\t : ')

    if kode == 'twd':
       try:
           print('\nAnda Memilih Buku "The Wish of Dragon"')
           jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
           harga = 50000
           jwb = jb*harga
           if jb >= 1 and jb <= 5 :
              disc = jwb * (15/100) #diskon 15%
           elif jb > 5 and jb <= 10 :
              disc = jwb * (25/100) #diskon 25%
           elif jb > 10 :
              disc = jwb * (50/100) #diskon 50%
           else:
               print('\nMaaf jumlah yang dimasukkan tidak cocok')
               hitung_harga()
       except ValueError:
           print("\nHarap Masukkan Nominal Yang Benar!\n")
           hitung_harga()

    elif kode == 'edn':
         try:
           print('\nAnda Memilih Buku "Emperor Domination"')
           jb = int(input('\nJumlah Buku\t\t\t\t\t : '))
           harga = 100000
           jwb = jb*harga
           if jb >= 1 and jb <= 5 :
              disc = jwb * (15/100) #diskon 15%
           elif jb > 5 and jb <= 10 :
              disc = jwb * (25/100) #diskon 25%
           elif jb > 10 :
              disc = jwb * (50/100) #diskon 50%
           else:
               print('\nMaaf jumlah yang dimasukkan tidak cocok')
               hitung_harga()
         except ValueError:
             print("\nHarap Masukkan Nominal Yang Benar!\n")
             hitung_harga()

    elif kode == 'lof':
         try:
           print('\nAnda Memilih Buku "Legend of Fution"')
           jb = int(input("\nJumlah Buku\t\t\t\t\t : "))
           harga = 150000
           jwb = jb*harga
           if jb >= 1 and jb <= 5 :
              disc = jwb * (15/100) #diskon 15%
           elif jb > 5 and jb <= 10 :
              disc = jwb * (25/100) #diskon 25%
           elif jb > 10 :
              disc = jwb * (50/100) #diskon 50%
           else:
               print('\nMaaf jumlah yang dimasukkan tidak cocok')
               hitung_harga()
         except ValueError:
           print("\nHarap Masukkan Nominal Yang Benar!\n")
           hitung_harga()

    elif kode == 'lot':
         try:
           print('\nAnda Memilih Buku "Love Letter"')
           jb = int(input("\nJumlah Buku\t\t\t\t\t : "))
           harga = 120000
           jwb = jb*harga
           if jb >= 1 and jb <= 5 :
              disc = jwb * (15/100) #diskon 15%
           elif jb > 5 and jb <= 10 :
              disc = jwb * (25/100) #diskon 25%
           elif jb > 10 :
              disc = jwb * (50/100) #diskon 50%
           else:
               print('\nMaaf jumlah yang dimasukkan tidak cocok')
               hitung_harga()
         except ValueError:
             print("\nHarap Masukkan Nominal Yang Benar!\n")
             hitung_harga()

    elif kode == 'mc7':
         try:
           print('\nAnda Memilih Buku "Miracle in Cell No 7"')
           jb = int(input("\nJumlah Buku\t\t\t\t\t : "))
           harga = 500000
           jwb = jb*harga
           if jb >= 1 and jb <= 5 :
              disc = jwb * (15/100) #diskon 15%
           elif jb > 5 and jb <= 10 :
              disc = jwb * (25/100) #diskon 25%
           elif jb > 10 :
              disc = jwb * (50/100) #diskon 50%
           else:
               print('\nMaaf jumlah yang dimasukkan tidak cocok')
               hitung_harga()
         except ValueError:
             print("\nHarap Masukkan Nominal Yang Benar!\n")
             hitung_harga()

    else:
        print('\nMaaf kode yang dimasukkan tidak cocok, silahkan masukkan ulang!\n')
        hitung_harga()

    ht = jwb - disc

    print("\n===============================================")
    print("                 Kwitansi               ")
    print("===============================================")
    print("Nama Pembeli, ",nama)
    print("Harga Total Sebelum Diskon\t : Rp. ",jwb)
    print("Potongan Harga           \t : Rp. ",disc)
    print("Harga Yang Harus di Bayar\t : Rp. ",ht)
    print(" ")
    print("===============================================")
    print("    Terima Kasih Sudah Berbelanja di Gramedia Kami           \n")

    exit = input('Apakah Anda ingin kembali ke menu utama? (y/n) : ')
    if exit == 'y':
       welcome()
    elif exit == 'n':
       keluar()
    else:
       keluar()

def back_to_menu():
    pilih = input('Apakah Anda ingin kembali ke menu utama? (y/n) : ')
    if pilih == 'y':
       menu()
    elif pilih == 'n':
       print('Anda memilih menutup aplikasi')
       keluar()
    else:
       print('Anda memasukkan nilai yang salah! Harap masukkan kembali')
       back_to_menu()

def keluar():   
    exit()

if __name__ == '__main__':
   while True:
       welcome()