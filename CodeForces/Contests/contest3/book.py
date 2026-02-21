n = int(input())

books = []

for _ in range(n):
    book = list(map(int, input().split()))
    books.append(book)


flag = True
flipped = False

for i in range(n - 1):
    b1, b2 = books[i]
    b11, b22 = books[i+1]

    if b2 >= b22:
        continue    
    elif b2 >= b11:
        books[i+1] = [b22, b11]
        continue
    elif b1 >= b22:
        continue
    elif b1 >= b11:
        books[i+1] = [b22, b11]
        continue
    else:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
