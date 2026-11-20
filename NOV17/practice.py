employee_name=input("Enter Your Name: ")
mothly_salary=int(input("Your Salary (Mothly): "))
annual_bonous_percentage=float(input("Annual Bonous (percentage): "))

annual_base_salary=mothly_salary*12
annual_bonous_money=(annual_bonous_percentage/100)*annual_base_salary
annual_compatation_money=annual_base_salary+annual_bonous_money

print(f"=========== {employee_name}'s Salary Breakdown===========")
print(f"My Anual Base Salary Is {annual_base_salary}")
print(f"My Anual Bonous Money Is {annual_bonous_money}")
print(f"My Total Anual Compation Is {annual_compatation_money}")
