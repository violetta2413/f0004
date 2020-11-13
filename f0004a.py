név = input('Hogy hívnak téged ? ')
kor = input('És hány éves vagy ? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té

év = input('Milyen évet írunk ? ')
év = int(év)

születési_év = év - kor
print(név, ', te ', születési_év, '-ban születtél.', sep='')