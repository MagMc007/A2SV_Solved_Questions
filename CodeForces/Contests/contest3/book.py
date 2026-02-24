n = int(input())

books = []

for _ in range(n):
    book = list(map(int, input().split()))
    books.append(book)


flag = True
height = max(books[0])

for w, h in books[1:]:
    if max(w, h) <= height:
        height = max(w, h)
    elif min(w, h) <= height:
        height = min(w, h)
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")

"""
    i was too attached to one approach
    change approach next time if it fails
    twice
"""
