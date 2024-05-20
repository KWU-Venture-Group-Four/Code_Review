def repeat_string(r, s):
    result = ''
    for char in s:
        result += char * r
    return result

# 입력 받기
t = int(input())
test_cases = []

for _ in range(t):
    r, s = input().split()
    r = int(r)
    test_cases.append((r, s))

# 출력
for r, s in test_cases:
    print(repeat_string(r, s))
