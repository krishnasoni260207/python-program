class employee:
    salary=1200000 #this is the class atribute.
    lang="py"
    def __init__(self,name,lang,salary):#dunder method which call autometicaly when 
        self.name=name                  #object is created
        self.lang=lang
        self.salary=salary
                        
        # print("my name is krishna soni.")

    @staticmethod 
    def info():
        print("good morning")
harry=employee("krishna","python",12000)#it is known as object.
harry.info()
print(harry.name,harry.lang,harry.salary)