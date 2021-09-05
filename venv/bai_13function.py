# Bài 13: Tính S(n) = x^2 + x^4 + … + x^2n
def sumn(n):
    s = 1
    x = 2
    for i in range(1, 6):
        s = s + pow(x, 2*i)
        print("i = " + str(i) + " => " + "s + pow(x, 2*i)=" + str(s))
        print("s = " + str(s))
    return s


print("sum of x^2 + x^4 + … + x^2n " + " is " + str(sumn(6)))
