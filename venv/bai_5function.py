#Bài 5: Tính S(n) = 1 + 1/3 + 1/5 + … + 1/(2n + 1)
def sum(n):
    s = 0
    for i in range(1, n):
        s = s + 1/(2*i + 1)
        print("i = " + str(i) + " => " + "1/(2*i + 1) =" + str(1/(2*i + 1)))
        print("s = " + str(s))
    return s


print("sum of 1 + 1/3 + 1/5 + … + 1/(2n + 1) " + " is " + str(sum(6)))
