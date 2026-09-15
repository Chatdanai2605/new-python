def divide (a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Exception: ", e)
    else:
        return resulta

a, b = map(int, input().split())
print(divide(a, b))
print("End of program")