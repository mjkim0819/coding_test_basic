# 분수 2개의 덧셈을 기약분수 형태로 나타내기

# 내 코드
def solution(denum1, num1, denum2, num2):
    denum = num1*denum2+num2*denum1
    num = num1*num2
    for i in range (num, 1, -1):
        if((denum % i == 0) and (num % i == 0)):
            denum = denum / i
            num = num / i
    answer = [denum, num]
    return answer
  
  
# 다른 사람의 gcd 사용 코드
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]
