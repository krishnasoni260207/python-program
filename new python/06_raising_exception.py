a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
if (b==0):
    raise ZeroDivisionError("hay,this code not take this kind of input for b")
else:
    print(f"Your ans is :{a/b}")