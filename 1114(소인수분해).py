n = int(input())
def prime(n):
    prime_list = [] # 소인수들을 담아둘 리스트
    
    while n % 2 ==0:
        prime_list.append(2)
        n = n//2
    divisor = 3
    while divisor ** 2 <=n:
        if n % divisor == 0:
            n = n//divisor
            prime_list.append(divisor)
            divisor +=2
    if n > 1: # 2와 3에서부터 시작한 홀수들로 나눠지지 못한 값이 있다면 소수이므로 추가
        prime_list.append(n)
    for i in prime_list:
        print(i)
        
prime(n)
------------------근데 시간초과로 통과 못함...
