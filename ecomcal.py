cn=input("Enter Your Name: ")
try:
    pa=float(input("Enter Your Purchase Amount: "))
    if pa<0:
        print("Enter A +ve number")
    bonus="Soryy Purchase More " if pa<1000 else "Congradulation!!"

    if pa<1000:
        dp=0
    elif pa>1000 and pa<49999:
        dp=5
    elif pa>5000 and pa<9999:
        dp=10
    elif pa>=1000:
        dp=20

    da=(dp/100)*pa

    tpa=pa-da

    print("==========Your Invoice===========")
    print(f"Bonus: {bonus}")
    print(f"Your Purchase amount: {pa}")
    print(f"Discount % and (amount): {dp} ({da:.2f})")
    print(f"Total Payble amount: {tpa}")


except ValueError:
    print("Enter A valid amount")