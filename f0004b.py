név = input('Hogy hínak téged ? ')
kor = input('És hány éves vagy ? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
év = input('Melyik évben járunk? ')

év = int(év)
születési_év = év - kor

print(név, ', te ', születési_év, '-ban születtél.', sep='')

érettségi_év = születési_év + 18
print(név, ', te ', érettségi_év, '-ban érettségizel.', sep='') 