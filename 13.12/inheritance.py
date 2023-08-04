class Calci:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print("sum is : ",(self.x+self.y))
    def sub(self):
        print("sub is : ",(self.x-self.y))
    def mul(self):
        print("mul is : ",(self.x*self.y))
    def div(self):
        print("div is : ",(self.x//self.y))
class Adv_Calci(Calci):
    def __init__(self,m,n):
        self.m=m
        self.n=n
        Calci.__init__(self,m,n)
        #super.__init__(m,n)
    def power(self):
        print("power is : ",(self.m)**(self.n))
    def percentage(self):
        print("percentage is : ",(self.m)%(self.n))

a=Adv_Calci(10,5)
a.add()
a.sub()
a.mul()
a.div()
a.power()
a.percentage()
        
