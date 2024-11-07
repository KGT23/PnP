n = int(input())  
A = set(map(int, input().split()))  # 리스트 A를 set으로 변환(중복제거)
m = int(input())  
B = list(map(int, input().split()))  

for num in B: # 찾아야 하는 값인 B의 값을 하나씩 i에 넣어서 A에서 탐색
    if num in A:
        print(1)
    else:
        print(0)
