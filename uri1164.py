# Import alphabet
import string
alphabet = (string.ascii_uppercase)

# Input Size of Triangle
x = int(input())
cont = 1

# Print Triangle
while cont <= x:
    print(alphabet[cont - 1] * cont)
    cont += 1


