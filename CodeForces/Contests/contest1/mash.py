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

