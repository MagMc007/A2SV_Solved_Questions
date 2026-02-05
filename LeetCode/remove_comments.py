# https://leetcode.com/problems/remove-comments/description/
# 722. Remove Comments
class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        code = []
        comment_flag = False
        currentStrip = ""

        # check for each given line
        for i in range(len(source)):
            line = source[i]
            j = 0  # to iterate over char in line

            if not comment_flag:
                # no comments opened, keep strip empty
                currentStrip = ""

            while j < len(line):
                if not comment_flag and j+1 < len(line) and line[j:j+2] == "/*":
                    # comment opened
                    comment_flag = True
                    j += 2
                elif comment_flag and j+1 < len(line) and line[j:j+2] == "*/":
                    # closing for an already opened comment
                    comment_flag = False
                    j += 2
                elif not comment_flag and j+1 < len(line) and line[j:j+2] == "//":
                    # single line comment, then pass to the next line
                    break
                elif not comment_flag:
                    # line is not a comment and no comments are opened
                    currentStrip += line[j]
                    j += 1
                else:
                    j += 1        

            if not comment_flag and currentStrip:
                # no opened and current strip is not empty
                code.append(currentStrip)
               
        
                    


                    

                
                
