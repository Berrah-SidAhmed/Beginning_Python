def erox():
    print("bienvunie")
    a = float(input("Put your wallet money :"))
    b = ["1/ Da to £", "2/ £ to Da", "3/ da to $ ", "4/ $ to da", "5/ £ to $", "6/ $ to £"]
    print(*b, sep="\n")
    c = input("choose what you want to convert :")
    a1 = "1"
    a2 = "2"
    a3 = "3"
    a4 = "4"
    a5 = "5"
    a6 = "6"

    if c == a1:
        tot = a * 200
        k=("{}£".format(tot))
        print(str.format(k))
    elif c == a2:
        tot1 = a / 200
        print("{} Da"  "%.2f".format(tot1))
    if c == a3:
        tot2 = a * 160
        print("{} $".format(tot2))
    elif c == a4:
        tot4 = a / 160
        print("{} Da".format(tot4))
    if c == a5:
        tot5 = a / 1.5
        print("{} $".format(tot5))
    elif c == a6:
        tot6 = a * 1.5
        print("{} Da".format(tot6))
while True:
    erox()




