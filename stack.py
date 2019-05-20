class stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
s=stack()
s.add("Mon")
s.add("Tues")
s.peek()
print(s.peek())
s.add("Fri")
s.add("thurs")
print(s.peek())
