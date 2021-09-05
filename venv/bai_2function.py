# Bài 2: Tính S(n) = 1^2 + 2^2 + … + n^2
def sum(n):
    s = 0
    for i in range(1, n):
        s = s + pow(i, 2)
        print("i = " + str(i) + " => " + "i^2 =" + str(pow(i, 2)))
        print("s = " + str(s))
    return s


print("sum of 1^2 + 2^2 + … + n^2 " + " is " + str(sum(6)))
