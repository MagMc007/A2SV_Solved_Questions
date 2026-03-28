# https://codeforces.com/problemset/problem/913/B
# B. Christmas Spruce
n = int(input())

# array of arrays to store the children of a parent
children = [[] for _ in range(n+1)]

for i in range(2, n+1):  # index 1: is the root
    parent = int(input())
    children[parent].append(i)


spruce = True

for i in range(1, n + 1):
    if len(children[i]) > 0:  # non-leaf
        leaf_child_count = 0
        
        for child in children[i]:
            # If the child has 0 children of its own, it is a leaf.
            if len(children[child]) == 0:
                leaf_child_count = leaf_child_count + 1

        # non leaf must have atleast 3 children 
        if leaf_child_count < 3:
            spruce = False
            break

if spruce:
    print("Yes")
else:
    print("No")
