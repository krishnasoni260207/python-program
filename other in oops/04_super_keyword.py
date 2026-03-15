class company:
    def __init__(self,name,company,m_name):
        self.name=name
        self.company=company
        self.m_name=m_name
        print("this is the constructor of company")
    def show1(self):
        print(f"the company name is {self.company}")

class manager(company):
    def __init__(self,name,company,m_name):
        super().__init__(name,company,m_name)
        print("this is the manager consructor")
   
    def show2(self):
        print(f"The {self.m_name} is the manager of {self.company}")

class employee(manager):
    def __init__(self,name,company,m_name):
        super().__init__(name,company,m_name)
        print("this is the employee constructor")
    def show(self):
        print(f"{self.name} works in {self.company} ")


b=employee("krishna","ITC","krish")
b.show()
b.show1()
b.show2()
# always pass same perameter of perent class constructor in 
# child class constructor.