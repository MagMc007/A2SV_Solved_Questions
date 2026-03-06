# https://leetcode.com/problems/shifting-letters-ii/description/
# 2381. Shifting Letters II

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        # initailize an array of 0 to hold the rotations
        ascii_arr = [0] * (len(s) + 1)

        # we do 1D update 
        for l, r, d in shifts:
            if d == 0:
                ascii_arr[l] -= 1
                ascii_arr[r + 1] += 1
            else:
                ascii_arr[l] += 1
                ascii_arr[r + 1] -= 1
        
        # compute the pref_sum
        pref = []
        curr = 0

        for i in ascii_arr:
            curr += i
            pref.append(curr)
 
        # prepare the actuall ascii for the chars
        s_ascii = [ord(ch) for ch in s]
        ans = ""

        for i in range(len(s)):
            # in the case of rotaions, find index
            new_ch = (s_ascii[i] - 97 + pref[i])%26 + 97
            ans += chr(new_ch)

        return ans


print(Solution().shiftingLetters(s = "abz", shifts = [[0,1,0],[1,2,1],[0,2,1]]))

# time => O(k,+n) k is the len(shifts) and n being the len(s)
# space => O(n)
