try:
    a=int(input("Enter a number:"))
    print(a)

except Exception as e:
    print(e)

else:
    print("i am inside else")

#Here if try block completly run than and than the else stetment run
#othrwise it so exception.