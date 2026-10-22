def rekap(nama, nilai_tugas, nilai_ujian):
    rata_rata = (nilai_tugas + nilai_ujian) / 2
    lulus = rata_rata >= 75

    print("Nama         :", nama)
    print("Nilai Tugas  :", nilai_tugas)
    print("Nilai Ujian  :", nilai_ujian)
    print("Rata-rata    :", rata_rata)
    print("Lulus        :", lulus)
    print("-" * 30)

rekap("Alfiansyah Sibyanurrizki", 80, 85)

rekap("Alfiansyah Sibyanurrizki", 60, 70)

rekap("Alfiansyah Sibyanurrizki", 70, 80)
