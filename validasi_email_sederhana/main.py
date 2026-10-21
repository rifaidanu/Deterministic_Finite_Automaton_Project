def validasi_email_dfa(email):
    state = 'q0'  #State awal
    for char in email:
        if state == 'q0': #Membaca username
            if char.isalnum() or char in ['_', '.']:
                state = 'q0'
            elif char == '@':
                state = 'q1'
            else:
                state = 'q_trap'
                
        elif state == 'q1': #Membaca karakter pertama domain
            if char.isalnum():
                state = 'q2'
            else:
                state = 'q_trap'
                
        elif state == 'q2': #Membaca nama domain
            if char.isalnum():
                state = 'q2'
            elif char == '.':
                state = 'q3'
            else:
                state = 'q_trap'
                
        elif state == 'q3': #Membaca huruf pertama ekstensi
            if char.isalpha():
                state = 'q4'
            else:
                state = 'q_trap'
                
        elif state == 'q4': #Membaca huruf berikutnya ekstensi
            if char.isalpha():
                state = 'q4'
            else:
                state = 'q_trap'
                
        elif state == 'q_trap':
            state = 'q_trap'
    return state == 'q4'

print("---=== PROGRAM VALIDASI EMAIL (DFA) ===---")
print("Ketik 'exit' untuk menghentikan program\n")

while True:
    input_email = input("Masukkan Email : ").strip()
    
    if input_email.lower() in ['exit']:
        print("\nProgram selesai")
        break
    
    if not input_email:
        print("Input tidak boleh kosong, coba lagi!\n")
        continue

    if validasi_email_dfa(input_email):
        print(f"Hasil: VALID (ACCEPT)\n")
        print("'Email memenuhi aturan sintaks email.\n")
    else:
        print(f"Hasil: TIDAK VALID (REJECT)\n")
        print("Email melanggar aturan sintaks email.\n")