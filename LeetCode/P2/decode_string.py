# https://leetcode.com/problems/decode-string/description/
# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        # 3 stacks: number, char, closing []
        stack_char = []

        for i in s:
            if i != "]":
                stack_char.append(i)
            else:
                # now we decode
                mult = ""  # the string to be multiplied

                while stack_char[-1] != "[":
                    mult = stack_char.pop() + mult

                # now we pop [
                stack_char.pop()

                # now we get the number
                numb = ""
                while stack_char and stack_char[-1].isnumeric():
                    numb = stack_char.pop() + numb
                mult = mult * int(numb)

                # add it to the stack char
                stack_char.append(mult)
        
        return "".join(stack_char)
    
# print(Solution().decodeString("100[leetcode]"))

                

# my mistake was not handling edge cases on the number and over dividing the chars
