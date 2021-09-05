# Bài 9: Tính T(n) = 1 x 2 x 3…x N
def sumn(n):
    s = 1
    for i in range(1, n):
        s = s * i
        print("i = " + str(i) + " => " + "s * i =" + str(s))
        print("s = " + str(s))
    return s


print("sum of 1 x 2 x 3…x N " + " is " + str(sumn(6)))
