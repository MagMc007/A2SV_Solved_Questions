n = int(input())
current = input()

"""
analysis:
conditions to stay in the river infinitely
    -'**' in str
    -'*<'
    -'>*'
    -'><'
    The guy wants to stay in the river as much time as possible, 
    we are asked for max time, so he must be forced to reach the shore
    > - the time needed is len - dx
    < - time needed is idx
    * - max of the left and the right
"""

if "**" in current or "*<" in current or ">*" in current or "><" in current:
    print(-1)
else:
    ans = 0
    i = 0
    while i < len(current) - 1:
        if not current[i] == current[i + 1]:
            if current[i + 1] == "*":
                ans = max(i + 1, len(current) - i - 1) + 1
            else:
                ans = max(i + 1, len(current) - i - 1)
        i += 1
        
    print(ans)