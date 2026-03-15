class company:
    def __init__(self,name,company,m_name):
        self.name=name
        self.company=company
        self.m_name=m_name
    def show1(self):
        print(f"the company name is {self.company}")

class manager(company):
   
    def show2(self):
        print(f"The {self.m_name} is the manager of {self.company}")

class employee(manager):
    def show(self):
        print(f"{self.name} works in {self.company} ")

# a=company("krishna","ITC")when we use inheritance concept
# a perent class constructor call in child class by defult so we not write
# b=employee()
b=employee("krishna","ITC","krish")
b.show()
b.show1()
b.show2()