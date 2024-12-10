"""paramet sifatida o'zida bitta son qabul qilsin masalan N soni 
N soning eng katta raqamini qiymat sifatida qaytarsin"""

N = input("N sonini kiriting: ").split()

def maxKatta(toplam):
    katta = toplam[0]
    for i in toplam:
        if katta < i:
            katta = i
    return katta

print(maxKatta(N))