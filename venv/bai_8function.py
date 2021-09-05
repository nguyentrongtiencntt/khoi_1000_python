# Bài 8: Tính S(n) = ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2
def sumn(n):
    s = 0
    for i in range(1, n):
        s = s + (2*i + 1)/(2*i + 2)
        print("i = " + str(i) + " => " + "(2*i + 1)/(2*i + 2) =" + str((2*i + 1)/(2*i + 2)))
        print("s = " + str(s))
    return s


print("sum of ½ + ¾ + 5/6 + … + 2n + 1/ 2n + 2 " + " is " + str(sumn(6)))
