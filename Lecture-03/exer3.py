hours = float(input("Enter the number of hours worked:"))
rate = float(input("Enter the number of hours worked:"))
if hours <=40:
    pay = (hours - 40) * hours_rate * 1.5 + (40 * hours_rate)
else:
    overtime = hours - 40
    gross_pay = (40 * rate) + (overtime * rate * 1.5)
    print("Total pay for the week: $",format(pay, ".2f"))