def n_sum(n):
    if (n==0) or (n==1):
        return n
    else:
        return n+n_sum(n-1)
n=int(input("Enter a number for sum: "))
print(f"Sum of n number is:{n_sum(n)}")            
      