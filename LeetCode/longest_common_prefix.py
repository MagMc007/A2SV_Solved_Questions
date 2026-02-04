class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]

        # index for slicing ans overriding the pref

        for item in strs[1:]:
            while pref:
                if item.startswith(pref):
                    break
                else:
                    pref = pref[:-1]

        return pref
