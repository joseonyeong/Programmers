def solution(n):
    
    num = n**(1/2)
    
    if num == int(num):
        return (num+1)**2
    else:
        return -1