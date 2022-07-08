# Bài 7: Tính S(n) = ½ + 2/3 + ¾ + …. + n / n + 1
def sum(n):
    s = 0
    for i in range(1, n):
        s = s + i / (i + 1)
        print("i = " + str(i) + " => " + "i / (i + 1) =" + str(i / (i + 1)))
        print("s = " + str(s))
    return s


print("sum of ½ + 2/3 + ¾ + …. + n / n + 1 " + " is " + str(sum(6)))
