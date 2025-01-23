class BrowserHistory:

    def __init__(self, homepage: str):
        self.currentPage = homepage
        self.backStack = []
        self.forwardStack = []

    def visit(self, url: str) -> None:
        self.backStack.append(self.currentPage)
        self.currentPage = url
        self.forwardStack.clear()

    def back(self, steps: int) -> str:
        while len(self.backStack) and steps != 0:
            self.forwardStack.append(self.currentPage)
            self.currentPage = self.backStack.pop()
            steps -= 1
        return self.currentPage

    def forward(self, steps: int) -> str:
        while len(self.forwardStack) and steps != 0:
            self.backStack.append(self.currentPage)
            self.currentPage = self.forwardStack.pop()
            steps -= 1
        return self.currentPage

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)