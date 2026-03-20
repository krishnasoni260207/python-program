l=[1,2,3,4,5]

def even(n):
    if(n%2==0):
        return True
    return False
even_no=filter(even,l)
#format of filter is:filter(function_name,list_name)
print(list(even_no))#this give only even number list.