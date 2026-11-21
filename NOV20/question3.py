correct_psw="python123"
MAX_ATTEMPTS=3
user_password=input("Enter The Password: ")
for att in range(0,MAX_ATTEMPTS+1):
    if user_password==correct_psw:
        print("Logimn Succesfull")
        att+=1
        break
    else:
        print(f"Remainig Attemts are {MAX_ATTEMPTS}")
        break
