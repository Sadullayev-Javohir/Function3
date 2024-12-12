"""parametr sifatida o'zida bitta son qabul qilsin masalan N soni 
N mert o'lchov birligida kirtiladi protsedura vazifasi shu mertni
necha mm, sm, dm, km eknaligni ekranga chiqarsin"""

N = int(input("O'lchov kiriting metrda: "))

def Measure(N):

    km = N // 1000
    dm = N // 10
    sm = N * 100
    mm = sm * 10

    return f"{N}m: {km}km\n{N}m: {dm}dm\n{N}m: {sm}sm\n{N}m: {mm}mm"

print(Measure(N))