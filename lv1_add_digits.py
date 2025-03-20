'''
    자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return
    하는 solution 함수를 만들어 주세요.
    예를들어 N = 123이면 1 + 2 + 3 = 6을 return
'''    
def solution(n):
    answer = 0
    # list함수 : 원소를 각각 끊어서 리스트로 만들어줌
    # map함수 : 해당 타입으로 변환
    arr = list(map(int, str(n)))
    for i in arr:
        if i != ' ':
            answer += i
    return answer

print(solution(123))