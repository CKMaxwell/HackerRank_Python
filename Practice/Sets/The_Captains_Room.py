# 20200703 - The Captain's Room
num = int(input())
orig = list(map(int, input().split()))
orig_set = set(orig)
for i in orig_set:
    count = 0
    for j in range(len(orig)):
        if orig[j] == i:
            count = count + 1
    if count == 1:
        ans = i
        break
print(ans)