from collections import Counter

# 입력 받기
word = input().strip().upper()

# 알파벳 빈도 계산
counter = Counter(word)

# 가장 많이 사용된 알파벳의 빈도 찾기
max_count = max(counter.values())

# 가장 많이 사용된 알파벳 찾기
most_common = [k for k, v in counter.items() if v == max_count]

# 결과 출력
if len(most_common) > 1:
    print("?")
else:
    print(most_common[0])
