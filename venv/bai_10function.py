# Bài 10: Tính T(x, n) = x^n
def sumn(n):
    t = 1
    x = 2
    for i in range(1, 4):
        t = t * x
        print("i = " + str(i) + " => " + "T * x =" + str(t))
        print("T = " + str(t))
    return t


print("sum of x^n " + " is " + str(sumn(6)))
