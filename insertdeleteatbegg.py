class Node:
    def __init__(self,x):
        self.data=x
        self.nextt=None
class S1: 
    def __init__(self):
        self.head=None
    def insertAtbeg(self):
            v=int(input("enter no:"))
            NewNode=Node(v)
            NewNode.nextt=self.head
            self.head=NewNode
    def delAtbeg(self):
        temp=self.head
        self.head=self.head.nextt
        temp.nextt=None
        
             
        
    def display(self):
            temp=self.head
            while(temp!=None):
                print(temp.data,end=" ")
                temp=temp.nextt
S=S1()
ch=0
while ch!=4:
    print("1.Insert at begining,2.delete at beg,3.display,4.search")
    ch=int(input())
    if ch==1:
        S.insertAtbeg()
        S.display()
    elif ch==2:
        S.delAtbeg()
        S.display()
    elif ch==3:
        S.display()
    else:
        print("Invalid choice")
        
