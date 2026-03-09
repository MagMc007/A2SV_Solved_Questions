n, B = map(int, input().split())
a = list(map(int, input().split()))

# Track number of even and odd 
even_count = 0
odd_count = 0

costs = []

for i in range(n - 1):
    if a[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
    if even_count == odd_count:
        cost = abs(a[i] - a[i+1])
        costs.append(cost)
        
costs.sort()

# pick the cheapest
cuts_made = 0
for cost in costs:
    if B >= cost:
        B -= cost
        cuts_made += 1
    else:
        break

print(cuts_made)