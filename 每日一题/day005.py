def aliquot(num):
        if '0' in str(num):
               return False
        else:
            for i in range(len(str(num))):
                  if num%int(str(num)[i]) == 0:
                       return True
                  else:
                       return False

def fibsNum():
        a = 0
        b = 1
        num_list = []
        while True:
                a,b = b,a+b
                if a > 10:
                       zc_status = aliquot(a)
                       if zc_status is True:
                                num_list.append(a)
                                if len(num_list) == 10:
                                        return num_list




print(fibsNum())