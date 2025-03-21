'''
    함수 solution은 정수 x와 자연수 n을 입력 받아, 
    x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트 리턴
    다음 제한 조건을 보고, 조건을 만족하는 함수
'''

def solution(x, n):
    answer = []
    num = 0
    for i in range(n):
        num += x
        answer.append(num)
    return answer
print(solution(2,5))