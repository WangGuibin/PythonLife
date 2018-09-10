# 我们知道1，2，4，8，16，32，64和128这8个数字利用加法可以得到1~255中的任意数字，如
# 21 = 1 + 4 + 16
# 192 = 64 + 128
# 编写一个函数输入1~255的数字，给出如何用1，2，4，8，16，32，64和128 的加法可以到这个数字。
# def fun(num):
#     ........
#
# >>> print(fun(155))
# 1 + 2 + 8 + 16 + 128
# >>> print(fun(3))
# 1 + 2
# >>> print(fun(8))
# 8

def func(num):
        arr = []
        base = [128,64,32,16,8,4,2,1]
        for i in base:
              if num >= i:
                 num -= i
                 arr.append(str(i))
        arr.reverse()
        print('+'.join(arr))

func(222)