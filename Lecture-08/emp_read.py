with open('employees.txt', 'r') as emp_file:
    for line in emp_file:
        print("Employee Name: " + line.strip())
        print("Employee ID: " + line.strip())
        print("Employee Department: " + line.strip())
        print()