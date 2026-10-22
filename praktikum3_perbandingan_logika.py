def periksa(nilai, kehadiran):
    syarat_nilai = nilai >= 75
    syarat_hadir = kehadiran >= 80
    lulus_and = syarat_nilai and syarat_hadir
    lulus_or = syarat_nilai or syarat_hadir

    print("Nilai = " + str(nilai) + ", Kehadiran = " + str(kehadiran) + "%")
    print("Nilai >= 75         :", syarat_nilai)
    print("Kehadiran >= 80     :", syarat_hadir)
    print("Lulus (pakai and)   :", lulus_and)
    print("Lulus (pakai or)    :", lulus_or)
    print()

periksa(82, 90)

periksa(70, 90)
