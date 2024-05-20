# 테스트 케이스 개수 입력
T = int(input())

# 각 테스트 케이스에 대한 처리
for _ in range(T):
    # 반복 횟수 R과 문자열 S를 입력받음
    R, S = input().split()
    R = int(R)  # R을 정수로 변환
    P = ''  # 새로운 문자열 P를 저장할 변수
    
    # 문자열 S의 각 문자를 R번 반복하여 P에 추가
    for char in S:
        P += char * R
    
    # 결과 출력
    print(P)
