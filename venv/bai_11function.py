# Tính mul(n) = 1.2.3….N
def mul(n):
    smul = 1
    x = 2
    for i in range(1, n):
        smul = smul * i
        print("i = " + str(i) + " => " + "smul * i =" + str(smul))
        print("smul = " + str(smul))
    return smul


print("sum of 1 x 2 x 3…x N " + " is " + str(mul(6)))

#
# def sumn(n):
#     sp = 0
#     x = 2
#     for j in range(1, 6):
#         sp = sp +mul(j)
#         print("j = " + str(j) + " => " + "sp +mul(j) =" + str(sp))
#         print("sp = " + str(sp))
#     return sp
#
#
#
# print("sum of 1 + 1.2 + 1.2.3 + … + 1.2.3….N " + " is " + str(sumn(6)))
