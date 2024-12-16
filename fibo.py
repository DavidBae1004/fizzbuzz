
#def fibo(num):
#    if num < 2:
#        return num
#    else:
#        return fibo(num-1) + fibo(num-2)
#print(fibo(5))

from math import sqrt

def fibo(num):
    """
    fibonacci sequence를 구하는 함수 입니다.
    """
  # 점화식 코드
    phi = (1 + sqrt(5)) / 2
  
    return round(pow(phi, num) / sqrt(5))

print(fibo(5))

