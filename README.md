# Praktikum-ddp

Program menghitung total harga barang berdasarkan dan jumlah pembelian
Prakasa Wira Mukti | 2409116054 | Sistem Informasi kelas B

FLOWCHART
![image](https://github.com/user-attachments/assets/0a540c9d-2df6-48a4-b8c5-0a8e4e60089a)



penjelasan
1.

def login():

Mendefinisikan fungsi bernama login.

2.

username_betul = 'Prakasa Wira Mukti'
nim_betul = '2409116054'

Menyimpan username dan NIM yang benar dalam variabel username_betul dan nim_betul.

3.

 while True:
 
 Memulai loop tak terbatas untuk meminta input dari pengguna.

4.

username = input('Masukan username: ')

nim = input('Masukan password: ')

Mengambil input dari pengguna untuk username dan nim.

5. 

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


Fungsi Login:

Ketika fungsi login() dipanggil, pengguna diminta untuk memasukkan username dan NIM.
Jika input username dan NIM sesuai dengan yang telah ditentukan (username_betul dan nim_betul), maka program mencetak pesan selamat datang dan keluar dari loop.
Jika input salah, program akan meminta pengguna untuk mencoba lagi dengan mencetak pesan kesalahan.

Input Harga dan Jumlah Pembelian:

Setelah login berhasil program akan meminta pengguna untuk memasukkan harga bakso dan jumlah pembelian.
Keduanya harus berupa angka; jika pengguna memasukkan nilai yang tidak valid (misalnya huruf atau simbol), program akan menangkap exception ValueError dan menampilkan pesan "Input tidak valid. Silakan masukkan angka yang benar."

Menghitung Total dan Diskon:

Program akan menghitung total harga berdasarkan harga per unit dan jumlah pembelian.
Jika total harga mencapai atau melebihi Rp 250.000, pengguna mendapatkan diskon 25%.
Program mencetak informasi mengenai diskon (jika ada) dan total harga setelah diskon.
Jika tidak ada diskon, program mencetak total harga yang harus dibayar.

Pertanyaan untuk Pembelian Selanjutnya:
Setelah menghitung dan mencetak total harga, pengguna ditanya apakah ingin melakukan pembelian lagi.
Jika pengguna menjawab "ya", program akan mengulangi proses input harga dan jumlah.
Jika pengguna menjawab selain "ya", program akan berhenti.

contoh output
Jika pengguna memasukkan username dan NIM yang benar, mereka akan melihat:

Selamat Datang, Prakasa Wira Mukti!

Harga Bakso (Rp): 100000

Jumlah pembelian: 3

Selamat, anda mendapatkan diskon= 75000.0      

Total harga Bakso untuk anda sekarang= 225000.0

Jika mereka memasukkan harga Rp 500.000 dan jumlah 1:

Selamat, anda mendapatkan diskon= 125000.0

Total harga Bakso untuk anda sekarang= 375000.0


BUKTI HASIL 
<img width="364" alt="Screenshot 2024-10-01 104152" src="https://github.com/user-attachments/assets/e041e125-8fb6-4b3f-bdeb-22f8231f8b3a">


