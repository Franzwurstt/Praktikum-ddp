# Praktikum-ddp
Prakasa Wira Mukti nim= 2409116054 
![image](https://github.com/user-attachments/assets/11d4ec02-0611-4d30-a485-8d02e0d6791f)
<img width="577" alt="Screenshot 2024-09-30 214203" src="https://github.com/user-attachments/assets/b6bc278d-b2e3-4857-9e6b-a717c42a7a2f">

penjelasan
1. baris pertama

def login():

Mendefinisikan fungsi bernama login.

2.baris 2-3

username_betul = 'Prakasa Wira Mukti'
nim_betul = '2409116054'

Menyimpan username dan NIM yang benar dalam variabel username_betul dan nim_betul.

3.baris 4

 while True:
 
 Memulai loop tak terbatas untuk meminta input dari pengguna.

4.baris 5-6

username = input('Masukan username: ')

nim = input('Masukan password: ')

Mengambil input dari pengguna untuk username dan nim.

5. baris 7

if username == username_betul and nim == nim_betul:

Memeriksa apakah username dan nim yang dimasukkan sesuai dengan yang benar.

6.

  print('Selamat Datang, ' + username + '!')
            break  
            
Jika login berhasil, mencetak pesan selamat datang dan keluar dari loop.

7.

        else:
            print('Mohon Maaf, username atau password salah. Coba lagi.')
Jika login gagal, mencetak pesan kesalahan dan kembali ke awal loop untuk meminta input lagi.
Bagian Pembelian Bakso

9.

    login()
Memanggil fungsi login untuk meminta pengguna masuk.

10.

while True:
Memulai loop tak terbatas untuk melakukan transaksi pembelian.

11.

try:
Memulai blok try untuk menangani potensi kesalahan saat input.

12.

 harga = float(input("Harga Bakso (Rp): "))
 jumlah = int(input("Jumlah pembelian: "))
Mengambil input harga dan jumlah pembelian, mengonversinya menjadi tipe data float dan int.

13.

total = harga * jumlah
Menghitung total harga dengan mengalikan harga dengan jumlah.

14.

if total >= 250000:
Memeriksa apakah total harga memenuhi syarat untuk mendapatkan diskon.

15.

diskon = total * 0.25
totaldiskon = total - diskon
Jika memenuhi syarat, menghitung diskon 25% dan total setelah diskon.

16.

 print(f'Selamat, anda mendapatkan diskon= {diskon}')
 print(f'Total harga Bakso untuk anda sekarang= {totaldiskon}')
Mencetak jumlah diskon dan total harga setelah diskon.

17.

 else:
     print(f'Tidak ada diskon, Total harga= {total}')
Jika tidak memenuhi syarat, mencetak total harga tanpa diskon.

18.

 lagi = input("Apakah Anda ingin melakukan pembelian lagi? (ya/tidak): ").strip().lower()
Menanyakan pengguna apakah ingin melakukan pembelian lagi dan memproses input.

19.

if lagi != 'ya':
break
Jika pengguna tidak ingin melanjutkan, keluar dari loop.

20.

except ValueError:
print("Input tidak valid. Silakan masukkan angka yang benar.")
Jika terjadi kesalahan konversi (misalnya, input bukan angka), mencetak pesan kesalahan dan kembali ke awal loop.

    

