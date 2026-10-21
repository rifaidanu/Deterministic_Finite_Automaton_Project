
def validasi_variabel(input_string):
    # Definisi state DFA
    q0 = "q0"       # State awal
    q1 = "q1"       # State penerima (accept)
    q_dead = "qd"   # State penolak (dead state)

    state = q0

    # Membaca setiap karakter pada input
    for karakter in input_string:
        if state == q0:
            # Karakter pertama harus berupa huruf atau underscore
            if ('a' <= karakter <= 'z') or \
               ('A' <= karakter <= 'Z') or \
               karakter == '_':
                state = q1
            else:
                state = q_dead

        elif state == q1:
            # Karakter selanjutnya boleh berupa huruf,
            # angka, atau underscore
            if ('a' <= karakter <= 'z') or \
               ('A' <= karakter <= 'Z') or \
               ('0' <= karakter <= '9') or \
               karakter == '_':
                state = q1
            else:
                state = q_dead

        elif state == q_dead:
            # Jika sudah ditolak, tetap berada di state penolak
            state = q_dead

    # Menentukan hasil akhir berdasarkan state
    if state == q1:
        return "VALID (ACCEPT)"
    else:
        return "TIDAK VALID (REJECT)"


# Program utama
print("=== PROGRAM VALIDASI NAMA VARIABEL DENGAN DFA ===")
input_string = input("Masukkan nama variabel: ")

hasil = validasi_variabel(input_string)
print("Hasil validasi:", hasil)
