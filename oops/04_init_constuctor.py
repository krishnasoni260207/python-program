class employee:
    salary=1200000 #this is the class atribute.
    lang="py"
    def __init__(self):#dunder method which call autometicaly when 
                        #object is created
        print("my name is krishna soni.")

    @staticmethod 
    def info():
        print("good morning")
harry=employee()#it is known as object.
harry.info()