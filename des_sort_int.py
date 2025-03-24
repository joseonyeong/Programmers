'''
    함수 solution은 정수 n을 매개변수로 입력 
    n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴
    예를들어 n이 118372면 873211을 리턴
'''

def solution(n):
    answer = 0
    arr = list(map(int, str(n)))
    arr.sort(reverse=True)
    answer = int(''.join(map(str,arr)))
    return answer

print(solution(118372))