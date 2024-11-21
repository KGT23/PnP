n = int(input())
def prime(n):
    prime_list = [] # 소인수들을 담아둘 리스트
    # 2로 나누어 떨어질 경우를 아래 3,5,7... 로 나눠 떨어지는 경우와 분리하여 계산 -> 이렇게 함으로써 짝수로 나누어 떨어지는 경우는 전부 거를 수 있음.
    while n % 2 ==0:
        prime_list.append(2)
        n = n//2 # n을 2로 나눈 몫으로 업데이트 하여 while의 조건을 만족하는동안(2로 나눠지는동안) 반복
    divisor = 3 # 나누는 수를 3으로 초기설정
    while divisor ** 2 <=n: # n을 소인수분해 할 때 작은 쪽의 소인수는 루트n을 넘지 못함 그리고 큰 쪽의 소인수는 작은쪽으로 나눠줄 때 어짜피 계산됨
        if n % divisor == 0:
            n = n//divisor 
            prime_list.append(divisor)
            divisor +=2 # 3에서 2씩 더하여 홀수에 대해 소인수를 갖는지 확인
    if n > 1: # 2와 3에서부터 시작한 홀수들로 나눠지지 못한 값이 있다면 소수이므로 추가
        prime_list.append(n)
    for i in prime_list:
        print(i)
        
prime(n)
------------------근데 시간초과로 통과 못함...
