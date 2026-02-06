# https://leetcode.com/problems/find-duplicate-file-in-system/description/
# 609. Find Duplicate File in System
class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        # my keys are he contents
        hash = {}

        for items in paths:
            dir, *files = items.split()
            for file in files:
                # unpack every content in hash
                name, content = file.split("(")
                
                if content in hash:
                    appendable = dir + "/" + name
                    hash[content].append(appendable)
                else:
                    hash[content] = [dir + "/" + name]
        print(hash)
        output = []    
        for key, val in hash.items():
            if len(val) > 1:
                output.append(val)
        return output
    
soln = Solution()
print(soln.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))