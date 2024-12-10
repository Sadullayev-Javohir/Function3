"""abs funksiyasini vazifasini bajaruvchi modul nomli funksiya tuzing funksiya 
vazifasi manfiy yoki musbat son kiritilsa musbat son sifatida qiymatini qaytarsin"""

a = int(input("A sonni kiriting: "))

def ABS(a):
    if a > 0:
        return(a)
    else:
        a *= -1
        return(a)

print(abs(a))