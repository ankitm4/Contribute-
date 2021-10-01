'''
class parrot:
    species="bird"

    def __init__(same,name,age):
        same.name=name
        same.age=age

dodo=parrot("dodo",32)
print("{} is a {} with age {}".format(dodo.name,dodo.__class__.species,dodo.age))

def solution(arr, n):
	for i in range(len(arr)):
		If arr[i] >= n:
			return i
	
	return i
A=[1,3,5,6]
B=7
print(A,k)
'''
#parent class
class birds:
    #class attribute
    Bird="They fly"
    
    #instance/object attribute
    def __init__(self):
        print("You are in parent class")

    #object method
    def meth(self,str):
        print("this is a object method {}".format(str))
    
    def qwer(self):
        print("this is a object method2")

#child class
class bird(birds):
    def __init__(self):
        super().__init__()
        print("hello")
    def hell(self):
        print("this is a child class")


parrot=bird()
parrot.hell()


    





