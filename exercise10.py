"""parametr sifatida o'zida ikkita son qabul qilsin a dan b gacha bo'lgan sonlarni a
soniga joriy yilni b soniga to'g'ilgan yilni kiritilsa inson necha yoshda ekanligini 
ekranga chiqarsin protsedura tuzing"""

def yosh(a, b):
    yosh = a - b
    return yosh

a = int(input("Hozir nechanchi yil: "))
b = int(input("Tug'ilgan yil: "))

print(yosh(a, b))