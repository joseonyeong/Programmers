'''
    대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
    s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 
    다르면 False를 return 하는 solution를 완성하세요.
    'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
    단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

    예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
'''

def solution(s):
    answer = True
    s = s.upper()   # 대소문자 관계없애려고 대문자로 변환
    PCount = 0  # P 개수 카운트
    YCount = 0  # Y 개수 카운트
    for i in s:
        if i == 'Y':    # Y라면
            YCount += 1 # count + 1
        elif i == 'P':  # P라면
            PCount += 1 # count + 1
    # if YCount == PCount:
    #     return True
    # else:
    #     return False
    return True if YCount == PCount else False

import numpy
def solution2(s):
    answer = True
    return True if s.upper().count('P') == s.upper().count('Y') else False
s = 'Hello Python'
print(solution2(s))