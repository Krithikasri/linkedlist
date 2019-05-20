class node:
    def __init__(self,data):
        self.data=data
        self.address=None
class sll:
    def __init__(self):
        self.head=None
    def insertatend(self):
        data=int(input())
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            return
        temp=self.head
        while temp.address:
            temp=temp.address
        
        temp.address=newnode
        newnode=None
    def delatend(self):
        temp=self.head
        
        while temp.address!=None:
            prev=temp
            temp=temp.address
        prev.address=None
            
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.address
s=sll()
ch=0
while ch!=4:
    print("1.Insert at end,2.del at end,3.display,4.search")
    ch=int(input())
    if ch==1:
        s.insertatend()
        s.display()
    elif ch==2:
        s.delatend()
        s.display()
    elif ch==3:
        s.display()
    else:
        print("Invalid choice")
