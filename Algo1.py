n = int(input())  # 첫째 줄에 주어지는 자연수 n
A = list(map(int, input().split()))  #
m = int(input())  # 다음 줄에 주어지는 자연수 m
B = list(map(int, input().split()))  # 그 다음 줄에 주어지는 m개의 정수 리스트

A.sort()

def bi_search_print_01(Array,n,K): # n은 사실 len(A)로 해도 상관없지만 이미input으로 n을 받았기 때문에 이용함
    l,r = 0, n-1
    while l <= r:
        m = (l+r)//2
        if Array[m] > K:
            r = m-1
        elif Array[m] < K:
            l= m+1
        else: 
            print(1) # Array[m] == K 이면 1을 출력하고 종료
            return
    print(0) # 전체를 탐색하는 동안 K를 찾지 못했으므로 0을 출력

for i in B: # B 리스트는 찾아야 하는 수 들의 목록이므로 i에 하나씩 넣어서 A안에 그 수가 있는지 탐색함
    bi_search_print_01(A,n,i)
    




