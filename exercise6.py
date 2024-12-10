"""paramet sifatida o'zida bitta belgi char qabul qiladigan belgilikkaTekshir nomli
funksiya tuzing funksiya vazifasi satr ichidagi belgilarni qaytarsin"""

a = input("Text kiriting: ")


def kattaHarf(a):
    symbol_belgilar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '\\', '|', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/']

    list = []
    for i in a:
        for j in symbol_belgilar:
            if i in j or i == " ":
                list.append(i)
    return(list)

print(kattaHarf(a))