'''
    자연수 n이 매개변수로 주어집니다. 
    n을 x로 나눈 나머지가 1이 되도록 하는 
    가장 작은 자연수 x를 return 하도록 solution 함수
'''

def solution(n):
    for i in range(1, n):  # 1부터 n-1까지 반복
        if n % i == 1:  # 나머지가 1이면
            return i  # 가장 작은 i 반환

print(solution(10))