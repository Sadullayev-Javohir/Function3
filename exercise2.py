"""isdigit funksiyasini vazifasini bajaruvchi RaqamlikkaTekshir nomli funksiya tuzing
funksiya vazifasi satr ichida raqam bo'lsa true aks xolda fasle qaytarsin"""

a = input("Text kiriting: ")


def RaqamlikkaTekshir(a):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list = []
    for i in a:
        for j in numbers:
            j = str(j)
            if i in j or i == " ":
                list.append(i in j)

    x = any(list)

    return(x)

print(RaqamlikkaTekshir(a))