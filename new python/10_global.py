a = 89
def num():
    global a
    a=3
    print(a)


num()
print(a)
#befor global output:
#89
#3
#after global output:
#3
#3
