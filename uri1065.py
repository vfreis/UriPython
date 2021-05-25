# Loop to inputs
count = 0
x1 = []
evens = 0

# Inputs
while count < 5:
    x1.append(float(input()))
    if x1[count] % 2 == 0:
        evens += 1
    count += 1

# Quantity of Even Numbers
print(f'{evens} valores pares')