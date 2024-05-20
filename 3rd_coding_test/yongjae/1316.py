def is_group_word(word):
    seen = set()  # 문자들이 나타난 순서를 기록하는 집합
    prev_char = None  # 이전 문자
    for char in word:
        if char != prev_char:
            if char in seen:
                return False
            seen.add(char)
        prev_char = char
    return True

# 입력 받기
n = int(input())
words = [input().strip() for _ in range(n)]

# 그룹 단어의 개수 세기
group_word_count = sum(1 for word in words if is_group_word(word))

# 결과 출력
print(group_word_count)
