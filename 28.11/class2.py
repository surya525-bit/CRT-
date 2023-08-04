class college:
    cname="vits"
    def __init__(self,rno,branch):
        self.rollno=rno        #instance variable
        self.branch=branch
    def display(self):
        print(self.rollno)
        print(self.branch,college.cname)
c=college(1,'cse')
print(c)
c1=college(2,'ece')
print(c1)
c.cname='vignan'
c.branch="csd"
c1.cname="vignan"
c.display()
c1.display()
print(c.cname,c1.cname)
print(c.cname,c1.cname)
























