# https://leetcode.com/problems/subdomain-visit-count/
# 811. Subdomain Visit Count
class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        # we will need a hash for every 
        # domain and its parents
        hash = {}

        for item in cpdomains:
            cnt, level = item.split()
            cnt = int(cnt)

            lvl_splited = level.split(".")
            if len(lvl_splited) == 2:
                # get the cp and parent
                first = lvl_splited[0] + "." + lvl_splited[1]
                second = lvl_splited[1]

                # check in hash, increment or add
                if first in hash:
                    hash[first] += cnt
                else:
                    hash[first] = cnt

                if second in hash:
                    hash[second] += cnt
                else:
                    hash[second] = cnt

            if len(lvl_splited) == 3:
                # get the cp and parent
                first = lvl_splited[0] + "." + lvl_splited[1] + "." + lvl_splited[2]
                second = lvl_splited[1] + "." + lvl_splited[2]
                third = lvl_splited[2]

                # check in hash, increment or add
                if first in hash:
                    hash[first] += cnt
                else:
                    hash[first] = cnt

                if second in hash:
                    hash[second] += cnt
                else:
                    hash[second] = cnt

                if third in hash:
                    hash[third] += cnt
                else:
                    hash[third] = cnt
        # now that all are in hash and are counted 
        # prepare output
        output = []
        for key, val in hash.items():
            output.append(str(val) +" " + key)
        
        return output

soln = Solution()
print(soln.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

