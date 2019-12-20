num = int(input("Enter a number: ")) 
fib = int(num-1)+int(num-2)
if num<0:
    print("incorrect input:")
elif num==1: 
    print("0")
elif num==2:
    print("1")
else: 
    print("fibonacci no of {0} is {1}" .format(num, fib))
