def penjumlahan(a,b):
    return a + b
def pengurangan(a,b):
    return a - b
def modulus(a,b):
    return a % b

bilangan1 = int(input('Masukkan bilangan pertama : '))
bilangan2 = int(input('Masukkan bilangan kedua : '))

print('\n')

print('Hasil penjumlahan dari bilangan tersebut ', penjumlahan(bilangan1,bilangan2))
print('Hasil pengurangan dari bilangan tersebut ', pengurangan(bilangan1,bilangan2))
print('Hasil modulus dari bilangan tersebut ', modulus(bilangan1,bilangan2))