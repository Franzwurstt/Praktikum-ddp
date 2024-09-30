def login():
    username_betul = 'Prakasa Wira Mukti'
    nim_betul = '2409116054'

    while True:
        username = input('Masukan username: ')
        nim = input('Masukan password: ')

        if username == username_betul and nim == nim_betul:
            print('Selamat Datang, ' + username + '!')
            break  
        else:
            print('Mohon Maaf, username atau password salah. Coba lagi.')

login()

while True:
    try:
        harga = float(input("Harga Bakso (Rp): "))
        jumlah = int(input("Jumlah pembelian: "))
        total = harga * jumlah

        if total >= 250000:
            diskon = total * 0.25
            totaldiskon = total - diskon
            print(f'Selamat, anda mendapatkan diskon= {diskon}')
            print(f'Total harga Bakso untuk anda sekarang= {totaldiskon}')
        else:
            print(f'Tidak ada diskon, Total harga= {total}')

        lagi = input("Apakah Anda ingin melakukan pembelian lagi? (ya/tidak): ").strip().lower()
        if lagi != 'ya':
            break
        
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka yang benar.")
       
    
    

    