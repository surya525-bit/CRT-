class calci:
    def __init__(self,x,y):
         self.x=x  #x-->instance variable
         self.y=y  #y-->instance variable
    def add(self):
        print("sum is : ",(self.x+self.y))
a=calci(10,20)
a.m=58  #m-->instance variable
a.add()
