class Stack:
    p1 = []

    def __init__(self, par):
        self.p1 = par

    def push(self, num: int):
        self.p1.append(num)
        return self.p1

    def pop(self):
        self.p1.pop()
        return self.p1

