class cal:
    def __init__(self,n):
        self.n=n

    def squre(self):
        print(self.n*self.n)
    def cube(self):
        print(self.n*self.n*self.n)
    def squreroot(self):
        print(self.n**(1/2))
    
c=cal(4)
c.cube()
c.squre()
c.squreroot()