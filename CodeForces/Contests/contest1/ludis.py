n = int(input())

rating = list(map(int, input().split()))
rank = []

rating_sorted = sorted(rating, reverse=True)

for i in rating:
    rank.append(rating_sorted.index(i) + 1)

print(*rank)