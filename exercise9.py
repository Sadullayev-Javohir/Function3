"""parametr sifatida o'zida bitta son qabul qilsin masalan N soni 
N ta son ekrandan kiritilsa ularning o'rta arifmetigi xisoblab qiymat sifatida 
qaytarsin
"""

n = int(input("n sonni kiriting: "))

def ortaArifmetik(n):
    count = 0
    averageArifmetik = 0
    for i in range(1, n + 1):
        averageArifmetik += i
        count += 1
        all = averageArifmetik / count
    return(all)

print(ortaArifmetik(n))