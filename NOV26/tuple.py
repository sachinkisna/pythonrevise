employees=(
    "emp1",
    "emp2",
    "emp3",
    "emp4",
    "emp1",
    "emp6",
    "emp7",
    "emp8",
    "emp9",
    "emp10",
)


print(f"first is {employees[0]} and last is {employees[-1]}")
print(f"total no. of employees  are {len(employees)}")
print(f"fiorst 4 employees {employees[:4]}")
print(f"emp1 appears hoe mny time {employees.count("emp1")}")
print(f"index of emp4 {employees.index("emp1")}")