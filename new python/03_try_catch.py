try:
    a=int(input("Enter a number:"))
    print(a)

except Exception as e:
    print(e)

print("thank you")
#in normal excution when error or exception occur than code excution is stop 
# #but in try and catch block the code excution is not stop 
# so the output of this code is
#output:
#enter a number:ererde ("not an int")
#it show exception
#thank you