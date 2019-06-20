def createstack():
    stack=[]
    return stack
def push(stack,item):
    stack.append(item)
    print(item,"pushed into the stack")
def pop(stack):
    a=len(stack)
    if a==0:
        return "str(maxsize)"//-1
    else:
        return stack.pop(0)
st=createstack()
ch=0
while ch!=5:
    ch=int(input())
    if ch==1:
        p=int(input())
        b=push(st,p)
        print(st)
    elif ch==2:
        b=pop(st)
        print(b)
        print(st)
