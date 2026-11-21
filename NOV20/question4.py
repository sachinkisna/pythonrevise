employees = [    {"name": "Rahul", "salary": 30000},    {"name": "Amit", "salary": 45000},    {"name": "Priya", "salary": 55000},    {"name": "Neha", "salary": 25000},    {"name": "Ravi", "salary": 60000}]


total_sal_exp=0
count=0
for name,salary in enumerate(employees):
    print(name,salary)
    total_sal_exp=total_sal_exp+salary
    count=+1
    
print(f"Total Number of employees: {count}")
print(f"Total Salary Expanditure={total_sal_exp}")
print(f"Average Salary={total_sal_exp/count}")

for name,salary in employees:
    if salary>40000:
        print(name)

   