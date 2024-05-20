# 단어 입력 받기
word = input().upper()  # 입력받은 단어를 모두 대문자로 변환
count = {}

# 알파벳별 사용 횟수 세기
for char in word:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

# 가장 많이 사용된 알파벳 찾기
max_count = max(count.values())
most_frequent = [k for k, v in count.items() if v == max_count]

# 가장 많이 사용된 알파벳이 여러 개인 경우 '?' 출력, 그렇지 않은 경우 해당 알파벳 출력
if len(most_frequent) > 1:
    print('?')
else:
    print(most_frequent[0])