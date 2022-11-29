def solution(n):
    answer = 0
    i = n // 2
    for a in range(0,i+1):
        a = a* 2
        answer = a + answer
    return answer
