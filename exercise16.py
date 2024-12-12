"""parametr sifatida ikkita qiymat qabul qiladigan masalan string
va char belgi berilgan satrda biz qidirgan belgi bo'lsa "siz 
qidirgan belgi bor " aks xolda "siz qidirgan belgi yo'q" so'zlarni
ekrangacha chiqaruvchi protsedura tuzing"""

def FindSymbol(text, char):

    symbol_belgilar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '\\', '|', ';', ':', "'", '"', '<', '>', ',', '.', '?', '/']
    for letter in text:
        for symbol in char:
            for listSymbol in symbol_belgilar:
                if letter in symbol and symbol in listSymbol:
                    return(letter in symbol_belgilar)
                

char = input("Belgi kiriting: ")
text = input('Matn kiriting: ')      


def checkFunction(check):
    check = True
    if check == FindSymbol(text, char):
        return("Bor")
    else:
        return("Yo'q")

print(checkFunction(FindSymbol(text, char)))