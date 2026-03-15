class company:
    def __init__(self,name,company):
        self.name=name
        self.company=company
    def show1(self):
        print(f"the company name is {self.company}")

    
class employee(company):
    def show(self):
        print(f"{self.name} works in {self.company} ")

# a=company("krishna","ITC")when we use inheritance concept
# a perent class constructor call in child class by defult so we not write
# b=employee()
b=employee("krishna","ITC")
b.show()
b.show1()