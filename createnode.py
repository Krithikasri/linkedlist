class node:
    def __init__(self,data):
        self.data=data
        self.nextt=None
N1=node(10)
N2=node(20)
N2=N1.nextt
print(N1.data)
