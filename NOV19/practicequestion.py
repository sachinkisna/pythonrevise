number=int(input("Enter a number: "))

if number>0 and number!=0:
    print(f"{number} is a positive")
    if number%2==0:
        print("It is a Even Number")
    else:
        print("It is a odd number")
    
elif number<0 and number!=0:
    print(f"{number} is a Negetive")
    if number%2==0:
            print("It is a Even Number")
    else:
        print("It is a odd number")
else:
    print(f"{number} is a 0")