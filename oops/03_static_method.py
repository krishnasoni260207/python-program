class employee:
    salary=1200000 #this is the class atribute.
    lang="py"

    @staticmethod 
    def info():
        print("good morning")
harry=employee()
harry.info()
#static method use when the self keyword is not needed
#and also work when there is no class atribute is use in 
#define function or method