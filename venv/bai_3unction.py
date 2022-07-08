# Bài 3: Tính S(n) = 1 + ½ + 1/3 + … + 1/n
def sum(n):
    s = 0
    for i in range(1, n):
        s = s + 1/i
        print("i = " + str(i) + " => " + "1/i =" + str(1/i))
        print("s = " + str(s))
    return s


print("1 + ½ + 1/3 + … + 1/n " + " is " + str(sum(6)))
