class employee:
    salary=1200000 #this is the class atribute.
    language="python"

    def info(self):
        print(f"The salary is {self.salary} and the language is {self.language}")
    # def info():
    #     print(f"The salary is {salary} and the language is {language}")
    # when we write this and call harry.info() 
    # its take as employee.info(harry) and so the code will give error. 
        

harry=employee()
harry.language="java" #this is the instant atribute.
harry.info()