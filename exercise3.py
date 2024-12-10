"""paramet sifatida o'zida bitta string qabul qiladigan findNumber nomli funksiya
tuzing funksiya vazifasi satr ichidagi raqamlarni ajratib qiymatini qaytarsin"""

a = input("Text kiriting: ")


def findNumber(a):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    list = []
    for i in a:
        for j in numbers:
            j = str(j)
            if i in j or i == " ":
                list.append(i)

    return(list)

print(findNumber(a))