# 随机生成一个由8位的数字组成的字符串，要求各位数字之和等于40。
# 例如：
# 54735781
# 01496488
# 27392296
# ......

#####  方案一  太耗性能了  显然不可取
# numList = []
# filterNum = []
# for i in range(1000000,100000000):
#         res = str(i)
#         if len(res) == 7:
#                 res = '0' + res
#
#         for j in range(len(res)):
#                 num = res[j:j+1]
#                 numList.append(num)
#         total = 0
#         for index in numList:
#                 total += int(index)
#                 if total == 40:
#                         filterNum.append(res)
#
# print(filterNum)

#### 方案二
import  random
import  xiaojiayu.Fibs as  T

def ranNumber():
    while True:
        numlist = []
        for i in range(8):
                ran = random.randint(0, 9)
                numlist.append(str(ran))
        result = []
        numCount = 0
        for j in numlist:
                numCount+=int(j)
        if numCount == 40:
                print(''.join(numlist))
                break


ranNumber()
fib = T.Fibs(100)
for each in fib:
        print(each)
