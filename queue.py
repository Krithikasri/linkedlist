class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None
    def enqueue(self):
        data=int(input())
        if self.last==None:
            self.head=node(data)
            self.head=self.last
            
        else:
            self.last.address=node(data)
            self.last=self.head.address
    def dequeue(self):
        if self.head==None:
            return None
        else:
            x=self.head.data
            self.head=self.head.address
            
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.address
q=queue()
ch=0
while ch!=4:
    print("1.enqueue,2.dequeue,3.display,4.stop")
    ch=int(input())
    if ch==1:
        q.enqueue()
        q.display()
    elif ch==2:
        q.dequeue()
        q.display()
    elif ch==3:
        q.display()
    else:
        print("invalid")
