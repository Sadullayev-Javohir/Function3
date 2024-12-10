"""paramet sifatida o'zida ikkita son qabul qilsin a dan b gacha bo'lgan sonlarni
yigindisini xisoblash qiymatini qaytarsin"""

a = int(input("a sonni kiriting: "))
b = int(input("b sonni kiriting: "))

def addition(a, b):
    add = 0

    for i in range(a, b + 1):
        add += i

    return(add)

print(addition(a, b))