"""paramet sifatida o'zida bitta son qabul qilsin masalan N soni 
N soning eng kichik raqamini qiymat sifatida qaytarsin"""

N = input("Sonlar kiriting: ").split()

def minNum(toplam):
    kichik = toplam[0]
    
    for i in toplam:
        if kichik > i:
            kichik = i
    return kichik

print(minNum(N))