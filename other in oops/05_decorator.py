# This program is about to data abstraction and encaptulation
class employee:
    a=1

    @classmethod#is use when class attribute is call insted of instance attribut.
    def show(cls):
        print(f"the class attribute is :{cls.a}")

    @property
    def name(self):
        return f"{self.lname} {self.fname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=employee()
e.a=45
 
e.name="krishna soni"
print(e.fname)
e.show()