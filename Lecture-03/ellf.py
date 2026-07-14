num_employees = int(input("Enter the number of employees: "))
if num_employees < 50:
    print("This is a small company .")
elif num_employees < 250:
    print("this is a medium_sized company. ")
elif num_employees >= 250:
    print("this is a large company. ")