"""paramet sifatida o'zida bitta string qabul qiladigan kattaHarf nomli funksiya 
tuzing funksiya vazifasi satr ichidagi katta harflarni qaytarsin"""


a = input("Text kiriting: ")


def kattaHarf(a):
    upper_letters= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
    list = []
    for i in a:
        for j in upper_letters:
            if i in j or i == " ":
                list.append(i)
    return(list)

print(kattaHarf(a))