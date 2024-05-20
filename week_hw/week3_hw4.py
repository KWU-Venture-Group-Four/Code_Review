def is_group_word(word):
    # 이미 나온 문자를 저장할 집합
    seen = set()
    prev_char = ''
    for char in word:
        # 현재 문자가 이미 나왔었고, 바로 이전 문자와 다르면 그룹 단어가 아님
        if char in seen and char != prev_char:
            return False
        seen.add(char)
        prev_char = char
    return True

n = int(input()) # 단어의 개수 입력
group_word_count = 0

for _ in range(n):
    word = input()
    if is_group_word(word):
        group_word_count += 1

print(group_word_count)