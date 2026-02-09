t = int(input())

for _ in range(t):
    n = int(input())
    year = input()
    if "2026" in year or "2025" not in year:
        print(0)
    elif "2025" in year:
        print(1)