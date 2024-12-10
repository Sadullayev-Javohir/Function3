"""paramet sifatida o'zida bitta string qabul qiladigan findKattaHarf nomli funksiya
tuzing funksiya vazifasi satr ichida katta harf bolsa true bo'lmasa false qiymatini
qaytarsin"""

a = input("Text kiriting: ")


def findKattaHarf(a):
    upper_letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    list = []
    for i in a:
        for j in upper_letters:
            if i in j or i == " ":
                list.append(i in j)
    x = any(list)
    return(x)

print(findKattaHarf(a))