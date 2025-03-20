'''
    자연수 n을 뒤집어 
    각 자리 숫자를 원소로 가지는 배열 형태로 리턴 
    예를들어 n이 12345이면 [5,4,3,2,1]을 리턴
'''

def solution(n):
    answer = []
    answer = list(map(int, str(n)))
    arrs = []
    for arr in reversed(answer):
        
        arrs.append(arr)
    return arrs
print(solution(12345))

# [5, 4, 3, 2, 1]