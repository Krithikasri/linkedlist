class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class sll:
    def __init__(self):
        self.head=None
    def insertatbeg(self):
        data=int(input())
        newnode=node(data)
        newnode.address=self.head
        self.head=newnode
    def insertatmid(self,prev,data):
        if prev is None:
            print("prev node is not there")
            return
        newnode=node(data)
        newnode.address=prev.address
        prev.address=newnode
    def delatmid(self,position):
        temp1=self.head
        c=1
        while c!=position-1:
            temp1=temp1.address
            c+=1
            return
        temp=temp1.address
        temp1.address=temp.address
        temp.address=None
            
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.address
        
s=sll()
s.head=node(10)
ch=0
while ch!=4:
    print("1.Insert at middle,2.del at mid,3.display,4.search")
    ch=int(input())
    if ch==1:
        data=int(input())
        prev=s.head
        s.insertatmid(prev,data)
        s.display()
    elif ch==2:
        print("Enter the position:")
        position=int(input())
        s.delatmid(position)
        s.display()
    elif ch==3:
        s.display()
    else:
        print("Invalid choice")
