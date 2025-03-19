'''
    정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, 
    solution을 완성해주세요.
'''

def solution(n):
    answer = 0 
    list = []   # 약수 넣을 리스트
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
    
    lenList = len(list)
    for j in range(0,lenList,1):
        answer += list[j]
        
    return answer

n = int(input("정수 입력: "))
print(solution(n))

    # 다른 풀이
def solution2(m):
    answer2 = 0
    return sum([i for i in range(1,m+1) if m % i == 0]) # 나눠서 0인 것들 더하라
print(solution2(12))
