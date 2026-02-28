def greter_num(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(f"The greter number out of three : {n1}")
    elif(n2>n1 and n2>n3):
        print(f"The greter number out of three : {n2}")
    elif(n3>n1 and n3>n2):
        print(f"The greter number out of three : {n3}")
    else:
        print("invalid")

n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
n3=int(input("Enter 3rd number: "))
greter_num(n1,n2,n3)