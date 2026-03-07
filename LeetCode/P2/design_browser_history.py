# https://leetcode.com/problems/design-browser-history/description/
# 1472. Design Browser History

# i need a doubly LL for backward traversal
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        # create home page
        self.curr = Node(homepage)  # this is my pointer

    def visit(self, url: str) -> None:
        # visiting
        on = Node(url, self.curr, None)

        # update currents next, and move pointer to it
        self.curr.next = on
        self.curr = self.curr.next
    
    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)