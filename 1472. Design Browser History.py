class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.index = 0

    def visit(self, url: str) -> None:
        # 1,2,3
        if self.index < len(self.history) - 1:
            self.index += 1
            self.history[self.index:] = [url]
        else:
            self.index+=1
            self.history.append(url)

    def back(self, steps: int) -> str:
        #1, 2, 3, 4
        if steps <= self.index:
            self.index -= steps
            return self.history[self.index]
        else:
            self.index = 0
            return self.history[0]

    def forward(self, steps: int) -> str:
        if len(self.history) - self.index - 1 >= steps:
            self.index += steps
            return self.history[self.index]
        else:
            self.index = len(self.history) - 1
            return self.history[-1]
if __name__=="__main__":
    a=BrowserHistory('l')
    a.visit('g')
    a.visit('f')
    a.visit('y')
    print(a.history)