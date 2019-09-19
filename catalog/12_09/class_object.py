'''class & objects
class name:
properties++
methods()
with in the class we have properties &methods
human=class-it is starts with capital letter
name,age,height=properties
speaking,running=methods
'''

class Human:
    def __init__(self,n,r):
        self.name=n
        self.role=r
    def work(self):
        if(self.role=='Developer'):
            print(self.name,"python Developer")
        elif(self.role=='Trainer'):
            print(self.name,"python Trainer")
#srav=Human("sravani","Developer")
srav=Human("sravani","Trainer")
srav.work()
