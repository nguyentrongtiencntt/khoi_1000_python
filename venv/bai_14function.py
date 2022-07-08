# Bài 14: Tính S(n) = x + x^3 + x^5 + … + x^2n + 1
def sumn(n):
    s = 1
    x = 2
    for i in range(1, 6):
        s = s + pow(x, 2*i+1)
        print("i = " + str(i) + " => " + "s + pow(x, 2*i+1)=" + str(s))
        print("s = " + str(s))
    return s


print("sum of x + x^3 + x^5 + … + x^2n + 1 " + " is " + str(sumn(6)))
