STATE_AWAL = "q0"
STATE_DITERIMA = ["q4", "q5", "q6", "q7", "q9", "q10", "q11"]

def kelompok(c):
    if "A" <= c <= "Z": return "L"
    if "1" <= c <= "9": return "D1"
    if c == "0": return "D0"
    if c == " ": return "SPASI"
    return None

TABEL_TRANSISI = {
    "qe": {"L": "qe", "SPASI": "qe", "D0": "qe", "D1": "qe"},
    "q0": {"L": "q1", "SPASI": "qe", "D0": "qe", "D1": "qe"},
    "q1": {"L": "q2", "SPASI": "q3", "D0": "qe", "D1": "qe"},
    "q2": {"L": "qe", "SPASI": "q3", "D0": "qe", "D1": "qe"},
    "q3": {"L": "qe", "SPASI": "qe", "D0": "qe", "D1": "q4"},
    "q4": {"L": "qe", "SPASI": "q8", "D0": "q5", "D1": "q5"},
    "q5": {"L": "qe", "SPASI": "q8", "D0": "q6", "D1": "q6"},
    "q6": {"L": "qe", "SPASI": "q8", "D0": "q7", "D1": "q7"},
    "q7": {"L": "qe", "SPASI": "q8", "D0": "qe", "D1": "qe"},
    "q8": {"L": "q9", "SPASI": "qe", "D0": "qe", "D1": "qe"},
    "q9": {"L": "q10", "SPASI": "qe", "D0": "qe", "D1": "qe"},
    "q10": {"L": "q11", "SPASI": "qe", "D0": "qe", "D1": "qe"},
    "q11": {"L": "qe", "SPASI": "qe", "D0": "qe", "D1": "qe"},
}

NOMOR_PLAT = "AA A5 R"

state_sebelum = "q0"
state_sekarang = "q0"

for i in NOMOR_PLAT:
    state_sebelum = state_sekarang
    state_sekarang = TABEL_TRANSISI[state_sekarang][kelompok(i)]

    print(f"{state_sebelum} --> {state_sekarang}")

    # if state_sekarang == "qe":
    #     break

print(state_sekarang)

if state_sekarang in STATE_DITERIMA:
    print("NOMOR PLAT VALID")
else:
    print("TIDAK VALID")