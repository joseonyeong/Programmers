'''
    정수를 담고 있는 배열 arr의 평균값을 return하는 함수
'''

def solution(arr):
    sum = 0
    answer = 0
    for i in arr:
        sum += i
        answer = sum / (len(arr))
    return answer
arr = [1,2,3,4]
print(solution(arr))