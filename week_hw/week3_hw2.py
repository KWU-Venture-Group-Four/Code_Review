# 문자열 입력 받기
string = input().strip()

# 문자열이 비어있는 경우, 단어의 개수는 0
if not string:
    print(0)
else:
    # 공백으로 단어를 구분하여 리스트 생성 후, 리스트의 길이(단어의 개수) 출력
    words = string.split()
    print(len(words))