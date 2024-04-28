print("APLIKASI PERHITUNGAN NILAI \n")
print("Silahkan masukan nilai Anda di bawah")
nilai_tugas = float(input("Nilai Tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))
nilai_akhir = 0.25 * nilai_tugas + 0.35 * nilai_uts + 0.40 * nilai_uas


if nilai_akhir > 85:
    grade = 'A'
elif nilai_akhir > 80:
    grade = 'A-'
elif nilai_akhir > 75:
    grade = 'B+'
elif nilai_akhir > 70:
    grade = 'B'
elif nilai_akhir > 65:
    grade = 'B-'
elif nilai_akhir > 60:
    grade = 'C+'
elif nilai_akhir > 55:
    grade = 'C'
elif nilai_akhir > 50:
    grade = 'C-'
elif nilai_akhir > 30:
    grade = 'D'
else:
    grade = 'E'

print("Nilai akhir: {:.2f}".format(nilai_akhir))
print("Grade: ", grade)