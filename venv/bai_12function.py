# Bài 12: Tính S(n) = x + x^2 + x^3 + … + x^n
def sumn(n):
    s = 1
    x = 2
    for i in range(1, 6):
        s = s + pow(x, i)
        print("i = " + str(i) + " => " + "s + pow(x, i)=" + str(s))
        print("s = " + str(s))
    return s


print("sum of x + x^2 + x^3 + … + x^n " + " is " + str(sumn(6)))
