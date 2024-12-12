"""parametr sifatida o'zida bitta string qabul qiladigan funksiya
tuzing funksiya vazifasi berilgan satr ichida nechta unli xarflar
sonini qiymat sifatida qaytarsin
"""

text = input('Matn kiriting: ')
unli = "EUIOA"

def UnliCount(text):
    count = 0
    for i in text:
        i = str(i)
        for u in unli:
            if i.lower() in u.lower():
                count += 1
    return(count)

print(UnliCount(text))