class twoD:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"Your 2D vector is:{self.i}i + {self.j}j")
class threeD(twoD):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show1(self):
        print(f"Your 3D vector is:{self.i}i + {self.j}j + {self.k}k")

a=twoD(2,3)
b=threeD(2,3,4)
a.show()
b.show1()
        
