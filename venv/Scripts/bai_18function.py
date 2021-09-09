# Bài 18: Tính S(n) = 1 + x^2/2! + x^4/4! + … + x^2n/(2n)!
def sumn(n):
    s = 0
    x = 2
    for i in range(1, n):
        s = s + pow(x, i) / (2 * i)
        print("i = " + str(i) + " => " + "s + pow(x, i) / (2 * i)=" + str(s + pow(x, i) / (2 * i)))
        print("s = " + str(s))
    return s


print("sum of 1 + x^2/2! + x^4/4! + … + x^2n/(2n)! = " + str(sumn(6)))
