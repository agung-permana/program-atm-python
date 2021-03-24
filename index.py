print("Selamat Datang Di ATM AGUNG BERSAMA")
print("Pilih Option :")
print("1. Cek Saldo")
print("2. Tarik Tunai")
print("3. Setor Tunai")
option = int(input("Silahkan Pilih : "))
if option == 1:
    print("Saldo Anda Rp. 200.000")
elif option == 2:
    print("Nominal : ")
    print("1. Rp. 100.000")
    print("2. Rp. 200.000")
    saldo = 200000
    option2 = int(input("Option : "))
    if option2 == 1:
        hasil = saldo - 100000
        print("Silahkan Ambil Uang Anda")
        print("Sisa Saldo Anda :", hasil)
        # print("Maaf, Saldo Anda Kosong.")
    elif option2 == 2:
        hasil = saldo - 200000
        print("Silahkan Ambil Uang Anda")
        print("Sisa Saldo Anda :", hasil)
    else:
        print("Silahkan Masukan Nominal Yang Benar!")
elif option == 3:
    saldo = 200000
    print("Isi Jumlah :")
    option3 = int(input("Masukan Jumlah Uang : "))
    hasil3 = saldo + option3
    print("Jumlah Saldo Anda Sekarang", hasil3)
else:
    print("Silahkan Masukan Nominal Yang Benar!")
