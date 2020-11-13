név = input('Hogy hívnak téged ? ')
kor = input('És hány éves vagy ? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
születési_év = 2020 - kor
print(név, ', te ', születési_év, '-ban születtél.', sep='')