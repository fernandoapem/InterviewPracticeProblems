class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        print(self.stack)
        if self.stack2 == []:
            while self.stack:
                self.stack2.append(self.stack.pop())
            print(self.stack2)
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    def peek(self) -> int:
        if self.stack2 == []:
            while self.stack:
                self.stack2.append(self.stack.pop())
            print(self.stack2)
            return self.stack2[len(self.stack2)-1]
        else: 
            return self.stack2[len(self.stack2)-1]

    def empty(self) -> bool:
        if self.stack == [] and self.stack2 == []:
            return True
        else: 
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()