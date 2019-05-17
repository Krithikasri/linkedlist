class node:
    def __init__(self,x):
        self.data=x
        self.address=None
class sll():
    def __init__(self):
        self.head=None
sl=sll()
sl.head=node("Mon")
N2=node("Tues")
N3=node("Wed")
sl.head.address=N2
N2.address=N3
temp=sl.head
while(temp!=None):
    print(temp.data,end=" ")
    temp=temp.address
