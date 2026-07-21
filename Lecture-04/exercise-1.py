print('----------------')
print('KPH\tMPH')
print('----------------')
for number in range(60, 131, 10):
    square = number*0.6214
    print(f"{number} \t {square:.1f}")