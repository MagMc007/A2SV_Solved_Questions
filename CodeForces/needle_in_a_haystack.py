# https://codeforces.com/problemset/problem/2174/A
# A. Needle in a Haystack
from collections import Counter

T = int(input())

for _ in range(T):
    s = input().strip()
    t = input().strip()

    count_t = Counter(t)
    count_s = Counter(s)

    # Check if s can be formed from t
    if any(count_s[ch] > count_t[ch] for ch in count_s):
        print("Impossible")
        continue

    # Remaining characters after removing s from t
    remaining = count_t - count_s   # i did not knwo we can operate on dicts like this

    new_t = "".join(ch * remaining[ch] for ch in sorted(remaining))

    # Merge s and remaining string in lexicographical order
    i ,j = 0, 0
    ans = ""

    while i < len(s) and j < len(new_t):
        if s[i] <= new_t[j]:
            ans += s[i]
            i += 1
        else:
            ans += new_t[j]
            j += 1

    # Append leftovers
    ans += "".join(s[i:])
    ans += "".join(new_t[j:])

    print(ans)

