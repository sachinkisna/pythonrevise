# mark=int(input("Enter your Mark"))

# if mark>90:
#     print("A")
# elif mark>70:
#     print("B")
# elif mark>60:
#     print("C")
# else:
#     print("D")


# user="Sachin"
# password="Sachin@4321"

# user_inp=input("Enter The User name: ")
# password_inp=input("EnterPassword: ")

# if user_inp==user and password_inp==password:
#         print("Login SuccesFull")
# else:
#     print("wrong userid/password")


# result="loggedin success" if user_inp==user and password_inp==password else "failedddd"

# print(result)

status="sasa"

match status:
    case "pending":
        print("Order Is waiting")
    case "shipped":
        print("Order is on the way")
    case _:
        print("Enter new value")