n = int(input())

rating = list(map(int, input().split()))
rank = []

rating_sorted = sorted(rating, reverse=True)

for i in rating:
    rank.append(rating_sorted.index(i) + 1)

print(*rank)

"""
Optimized NlogN
    copy the arr, maintain a dictionary of the count of elemts grater than 
    an element, sort them, 
    to add to the dict: you will do the num: len(dict) + index + 1(if not in the dic)
    meaning you are getting the number of elemnts greater than the current number

    now iterate over the the original and access the value in dict
"""