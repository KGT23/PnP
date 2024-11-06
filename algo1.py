# 입력 받기
n = int(input().strip())  # 첫째 줄에 주어지는 자연수 n
A = set(map(int, input().strip().split()))  # 다음 줄에 주어지는 n개의 정수 (집합으로 변환하여 중복 제거 및 검색 속도 향상)

m = int(input().strip())  # 다음 줄에 주어지는 자연수 m
B = list(map(int, input().strip().split()))  # 그 다음 줄에 주어지는 m개의 정수 리스트

# 결과 출력
for number in B:
    if number in A:
        print(1)
    else:
        print(0)
