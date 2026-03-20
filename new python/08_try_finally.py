def main():
    try:
        a=int(input("Enter a number:"))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("i am inside else")

main()
# finally block is always run if we not use function 
#but for function when try and finally inside the function than if any part of 
#function can "return" value than other code of function can not change
#but finally keyword can over come this and if return value in function than also finally run
