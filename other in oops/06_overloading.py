class number:
    def __init__(self,n):
        self.n=n

    def __add__(self,self1):
        return self.n+self1.n
    
n=number(4)
m=number(5)
print(n+m)