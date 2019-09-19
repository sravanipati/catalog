class Register:
	print("welcome")
	X=7875
	n="srav"
obj=Register()
print(obj)
print(obj.X)
print(obj.n)

class Register:
	def__init__(self,name,des):
		self.name=name
		self.des=des
	def login(self):
		print("login completed "+self.name)
object=Register("sravani","lea")

print(object.name)
object.login()
