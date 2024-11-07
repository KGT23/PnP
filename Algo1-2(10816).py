n = int(input())  # 상근이가 가지고 있는 카드의 수
Have_list = list(map(int, input().split()))  # 상근이가 가지고 있는 카드 목록
m = int(input())
Card_list = list(map(int, input().split())) # 상근이가 가진 카드에서 몇개가 있는지 찾아야할 목록

count = {} # 카드를 key로 해당 카드의 수를 value로 하는 딕셔너리

for i in Have_list: # 찾아야 하는 카드가 딕셔너리안에 있다면 (in 연산자는 딕셔너리 key를 기준으로 검색함)
    if i in count: 
        count[i]+=1 # 해당 key의 value 1증가
    else:
        count[i]=1
        
for j in Card_list: 
    if j in count: # j는 찾아야 하는 카드
        print(count[j],end=' ')
    else:
        print(0, end=' ')
