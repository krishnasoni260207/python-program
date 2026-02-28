def patten(n):
    i=n
    for i in range(n,0,-1):#when we enter a limit in greter to smaller alwayes give stap.
        print("*" *i,end="" )
        print(" ")
n=int(input("Enter a number for patten: "))
patten(n)