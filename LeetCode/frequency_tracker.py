# https://leetcode.com/problems/frequency-tracker/description/
# 2671. Frequency Tracker

class FrequencyTracker:
    # I don't really need the array to do the functionality
    def __init__(self):
        # keep count
        self.cnt = {}
        self.freq_count = {} # for avoiding O(n) in the end

    def add(self, number: int) -> None:
        # get the current count of the number
        old_cnt = self.cnt.get(number, 0)

        if old_cnt > 0:
            # update frequency
            # the old count has now lost a number
            self.freq_count[old_cnt] -= 1
            if self.freq_count[old_cnt] == 0:
                del self.freq_count[old_cnt]

        # old_cnt + 1 frequency key will now have one elemt added to it 
        self.cnt[number] = old_cnt + 1 # number will have its old count increased 
        # in the freq the existing 
        self.freq_count[old_cnt + 1] = self.freq_count.get(old_cnt + 1, 0) + 1
         
    def deleteOne(self, number: int) -> None:
        if number not in self.cnt:
            return
        
        # using the current frequency
        old_cnt = self.cnt[number]
        self.freq_count[old_cnt] -= 1
        if self.freq_count[old_cnt] == 0:
            del self.freq_count[old_cnt]

        if old_cnt == 1: # no new addition to freq_cnt
            self.cnt.pop(number)
        else:
            self.cnt[number] = old_cnt - 1
            # a new addition
            self.freq_count[old_cnt - 1] = self.freq_count.get(old_cnt - 1, 0) + 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count.get(frequency, 0) > 0



# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(1)
# obj.deleteOne(1)
# param_3 = obj.hasFrequency(1)

# print(param_3)
