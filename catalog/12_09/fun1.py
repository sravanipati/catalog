'''def sample():
    print("hello function")
    def sam():
        print("inside function")
    sam()
sample()'''

'''#a=int(input())
#b=int(input())
#c=int(input())
def sample(a,b,c):
#def sample(a,b,c=10):
    if(a==b and b==c and c==a):
        print(0)
    elif(a!=b and b!=c and a!=c):
        print(a+b+c)
    else:
        if(a==b):
            print(c)
        elif(b==c):
            print(a)
        else:
            print(b)
#sample(a,b,c)
#sample(2,3)=2+3+10
#sample(2,3,20)=2+3+20
sample(a=2,b=3,c=2)

'''

def l(s,b,*var):
    #def l(*var,s=100,b=100) s&b are default values
    #variable length argument  * meaning is all
    for i in var:
        print(i)
    print(s,b)
l(10,2,3,5,6,7,8,5,4,3,4,6,7,7,4,23,34,5,6,5,1)# s=10 in the last position
