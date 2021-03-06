# Shalommita Pranatantri
# 71200640
# INFORMATIKA - UKDW
# STRUKTUR KONTROL PERULANGAN (LOOPING)

# Soal: Ibu Nita sebagai dosen diminta untuk menghitung nilai dari 3 nilai (nilai harian, uts, dan uas) 
# Syarat penilaian berdasarkan rentang nilai

# INPUT
# Input berapa kali data akan dihitung
# Input nilai harian, uts, dan uas

# PROSES
# Deklarasi Fungsi total_nilai
def total_nilai(harian,uts,uas):
    harian=int(harian)*0.3
    uts=int(uts)*0.3
    uas=int(uas)*0.4

    totalan = harian+uts+uas
    return totalan

# Deklarasi Fungsi Percabangan
def cabang(nilai):
    huruf = ""
    if (nilai>=0 and nilai<20):
        huruf="E"
    elif (nilai>=20 and nilai<40):
        huruf="D"
    elif (nilai>=40 and nilai<60):
        huruf="C"
    elif (nilai>=60 and nilai<80):
        huruf="B"
    elif (nilai>=80 and nilai<=100):
        huruf="A"
    return huruf

# Deklarasi Fungsi Perulangan
def ulang():
    hasil_ulang=0
    input_data = int(input("Data dihitung berapa kali? ")) #0,1
    for i in range(input_data):
        print("---------- NIlai ke-",i+1,"----------")
        harian=input("Nilai Harian: ")
        uts=input("Nilai UTS: ")
        uas=input("Nilai UAS: ")

        #Pemanggilan fungsi penjumlahan
        hasil_ulang += int(total_nilai(harian,uts,uas))
    return hasil_ulang/input_data

# OUTPUT
# Pemanggilan Fungsi Perulangan
total=ulang()
print("---------- Total Nilai ----------")
print("Total nilai yang diperoleh: ",total)

# Pemanggilan Fungsi Percabangan
print("Total nilai dalam huruf: ",cabang(total))
