"""parametr sifatida o'zida bitta string qabul qiladigan teskariSatr nomli protsedura
tuzing protsedura vazifasi berilgan satrni teskarisiga chiqarsin"""

def teskariMatn(s):
    teskariGap = ""
    for letter in s:
        teskariGap =  letter + teskariGap
    return teskariGap

print(teskariMatn("Salom"))