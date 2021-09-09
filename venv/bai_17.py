# Tính S(n) = x + x^2/2! + x^3/3! + … + x^n/N!
def sumn(n):
    s = 0
    x = 2
    for i in range(1, n):
        s = s + pow(x, i) / i
        print("i = " + str(i) + " => " + "s + pow(x, i) / i=" + str(s))
        print("s = " + str(s))
    return s


print("sum of x + x^2/2! + x^3/3! + … + x^n/N! = " + str(sumn(6)))
