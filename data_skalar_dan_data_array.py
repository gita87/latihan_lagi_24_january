print('hellow mameeen')

# belajar data skalar
a = ['rina','rani','reno','retno','rana','rini']

print(a)

a1 = 'rina'
a2 = 'rani'
a3 = 'reno'
a4 = 'retno'
a5 = 'rana'
a6 = 'rini'
print('\nini spasi')
print(a1)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)

print('\nbelajar data array')

anak = ['rina','rani','reno','retno','rana','rini']

print(anak)
anak.append('egi')
print(anak)

print('\nsapa anak ke 2')
print(f'hai {anak[1]}')

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}')

print('\ncara lain')
for a in range (0, len(anak)):
    print(f'hai {a}')
    print(f'hai {anak}')
    print(f'hai {anak[a]}')

print('\n cara lain jilid 2')
for a in range (0, len(anak)):
    print(f'hai {anak[a]}')

print('\n testing testing')
tes_string = 'iga '
print(tes_string,'panjangnya adalah', len(tes_string))

nama = input('budi')
