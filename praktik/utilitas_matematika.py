def luas_persegi_panjang(p, l):
    return p * l


def luas_segitiga(a, t):
    return 0.5 * a * t


def jumlah_n(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif")

    total = 0

    for i in range(1, n + 1):
        total += i

    return total


def faktorial(n):
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n harus berupa bilangan bulat nonnegatif")

    hasil = 1

    for i in range(2, n + 1):
        hasil *= i

    return hasil


def tampilkan_menu():
    print("\n=== UTILITAS MATEMATIKA ===")
    print("1. Luas persegi panjang")
    print("2. Luas segitiga")
    print("3. Jumlah 1 sampai n")
    print("4. Faktorial")
    print("5. Keluar")


def input_angka(pesan):
    while True:
        try:
            return float(input(pesan))
        except ValueError:
            print("Input harus berupa angka. Coba lagi.")


def input_bilangan_bulat(pesan):
    while True:
        teks = input(pesan).strip()

        try:
            n = int(teks)

            if n < 0:
                print("Bilangan harus nonnegatif.")
                continue

            return n

        except ValueError:
            print("Input harus berupa bilangan bulat nonnegatif.")


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih operasi (1-5): ").strip()

        if pilihan == "1":
            p = input_angka("Panjang: ")
            l = input_angka("Lebar: ")
            print("Luas persegi panjang =", luas_persegi_panjang(p, l))

        elif pilihan == "2":
            a = input_angka("Alas: ")
            t = input_angka("Tinggi: ")
            print("Luas segitiga =", luas_segitiga(a, t))

        elif pilihan == "3":
            n = input_bilangan_bulat("Masukkan n: ")
            print("Jumlah 1 sampai", n, "=", jumlah_n(n))

        elif pilihan == "4":
            n = input_bilangan_bulat("Masukkan n: ")
            print("Faktorial", n, "=", faktorial(n))

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")


if __name__ == "__main__":
    main()