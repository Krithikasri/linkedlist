class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class stack:
    def __init__(self):
        self.head=None
    def push(self):
        data=int(input())
        if self.head==None:
            self.head=node(data)
        else:
            newnode=node(data)
            newnode.address=self.head
            self.head=newnode
    def pop(self):
        if self.head==None:
            return None
        else:
            
            pop=self.head
            self.head=self.head.address
            pop.address=None
    
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.address
s=stack()
ch=0
while ch!=4:
    print("1.push,2.pop,3.display,4.quit")
    ch=int(input())
    if ch==1:
        s.push()
        s.display()
    elif ch==2:
        s.pop()
        s.display()
    elif ch==3:
        s.display()
    else:
        print("Invalid choice")
