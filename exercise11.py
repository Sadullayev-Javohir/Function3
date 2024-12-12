"""parametr sifatida o'zida bitta son qabul qilsin masalan N soni 
N kun boshidan boshlab qanchadir sekun o'tganligni bildirsin
protsedura vazifasi bizga ayni vaqtda soat nechchi bo'lganlini
ekranga chiqarsin"""

def findTime(N):
    SecondInDay = 24 * 60 * 60

    totalSeconds = N %  SecondInDay

    hours = totalSeconds // 3600
    minutes = (totalSeconds % 3600) // 60

    return f"Ayni vaqtda {hours:02d}:{minutes:02d}"

N = int(input("Sekundni kiriting: "))
print(findTime(N))
