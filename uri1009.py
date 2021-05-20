name = input()
salary = float(input())
sales = float(input())

sales *= 0.15
salary += sales

print('TOTAL = R$ %0.2f' %salary)
print(f'TOTAL = R$ {salary:.2f}')
