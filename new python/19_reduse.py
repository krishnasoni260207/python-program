from functools import reduce
l=[1,2,3,4,5]
list = lambda a,b:a+b
list1 = lambda a,b:a*b
print(reduce(list,l))#also use for multiply
print(reduce(list1,l))