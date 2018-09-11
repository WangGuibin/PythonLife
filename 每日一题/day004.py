#斐波那契数中有些数字是可以被其各位数字之和整除的，例如：
# 144可以被1+4+4整除。
# 要求求出前10个这样的斐波那契数（不包括一位数1, 2, 3, 5, 8）。


# 666 -> 6+6+6 = 18  获取各位之和
def aliquot(num):
        temp = 0
        for i in range(len(str(num))):
                 temp += int(str(num)[i])
        return temp

# 1,1,2,3,5,8,13,21...
def fibsNum():
        a = 0
        b = 1
        num_list = []
        while True:
                a,b = b,a+b
                if a > 10:
                       div = aliquot(a)
                       if a%div == 0:
                                num_list.append(a)
                                if len(num_list) == 10:
                                        return num_list




print(fibsNum())
